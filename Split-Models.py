import re

#read from file
f_in = open("comb_01.pdbqt", "r")

#read name list file
name_file = open("name_list.txt","r")
name_list = name_file.readlines()
new_name_list = []
for name in name_list:
    new_name_list.append(name.replace("\n", ""))


temp_data =[]
current_model = ""
#store lines to a array form
data_rows = f_in.readlines()

#check each line
for row in data_rows:
    
    #if the line contains MODEL string
    if row.find('MODEL') == 0:
        
        #if model is not the same as last process
        if row != current_model:            
            if len(temp_data) > 1:
                number_list = re.findall('\d+', current_model)
                model_num = int(number_list[0])
                file_path = number_list[0]+"_"+new_name_list[model_num-1]+".pdbqt"
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
if len(temp_data) > 1:
    number_list = re.findall('\d+', current_model)
    model_num = int(number_list[0])
    file_path = number_list[0]+"_"+new_name_list[model_num-1]+".pdbqt"
    file_path = file_path.strip()
    file_path = file_path.replace("\n", "")
    f_out = open(file_path, "w")
    f_out.writelines(temp_data)
    f_out.close()
   
