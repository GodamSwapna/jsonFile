import json
json_string='''{
            "a":1,
            "a":2,
            "a":3, 
            "a":4,   
            "b":1, 
            "b":2
            }'''
python_string=json.loads(json_string)
print(type(python_string))
dic={}
for key,value in python_string.items():
    dic[key]=value
print(dic)