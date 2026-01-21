"""  
JSON - Javascript Object Notation

"""
# import json
# student = {
    
#     "id" : "S001",
#     "name" : "Shyam",
#     "marks" : 65
    
#     }

# json_data = json.dumps(student)      # dumps -> it converts any types of data into json format, it takes only one parameter
# print(json_data)



import json
student = {
    
    "id" : "S001",
    "name" : "Shyam",
    "marks" : 65
    
    }
with open("C:/Users/acer/Desktop/Python/File_Handling/text.json","w") as f:
    json.dump(student,f)   # it takes two parameter, which file to dump, where to dump
    

import json
with open("C:/Users/acer/Desktop/Python/File_Handling/text.json","r") as f:
    original_format = json.load(f)    # it converts the data of json format into original format
print(original_format)
