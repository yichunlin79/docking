f_in = open("comb_01.pdbqt", "r")

temp_data =[]
current_model = ""
data_rows = f_in.readlines()

for row in data_rows:
    
    if row.find('MODEL') == 0:              
        #if model is not the same as last process
        if row != current_model:
            if len(temp_data) > 1:
                file_path = current_model+".pdbqt"
                file_path = file_path.strip()
                file_path = file_path.replace("\n", "")
                f_out = open(file_path, "w")
                f_out.writelines(temp_data)
                f_out.close()
                temp_data.clear()               
            current_model = row
            temp_data.append(row)
        #if model is the same as last one
        else:
            print("model duplicated!"+row)
            temp_data.append(row)
    else:
        temp_data.append(row)
        
#last model        
if len(temp_data) != 0:
    file_path = current_model+".pdbqt"
    file_path = file_path.strip()
    file_path = file_path.replace("\n", "")
    f_out = open(file_path, "w")
    f_out.writelines(temp_data)
    f_out.close()
