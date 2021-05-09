f_in = open("comb_01.pdbqt", "r")

temp_data =[]
current_model = ""
data_rows = f_in.readlines()

for row in data_rows:
       
    temp_data.append(row)
    if row.find('MODEL') == 0:  
        current_model = row
        #if model is not the same as last one
        if row != current_model:
            #only create new files when data is not empty
            if len(temp_data) != 0:
                file_path = current_model+".pdbqt"   #create .pdbqt file
                file_path = file_path.strip()        #remove space charactors
                file_path = file_path.replace("\n", " ")  #remove newline 
                temp_data.pop()   #pop the last row  --> model
                f_out = open(file_path, "w")
                f_out.writelines(temp_data)
                f_out.close()
                temp_data.clear()
                temp_data.append(current_model) #store model
            
        #if model is the same as last one
        else:
            print("Model duplicated: "+row) #show which model is duplicated