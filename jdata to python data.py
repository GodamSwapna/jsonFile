import json

jobj_dict =  '{"name": "David", "age": 6, "class": "I"}'
jobj_list =   '["Red", "Green", "Black"]'
jobj_string = '"Python Json"'
jobj_int = '1234'
jobj_float =  '21.34'
# jobj_complex=2+3j

python_dict=json.loads(jobj_dict)
python_list=json.loads(jobj_list)
python_string=json.loads(jobj_string)
python_int=json.loads(jobj_int)
python_float=json.loads(jobj_float)

print("python dict:",python_dict)
print("python list:",python_list)
print("python string:",python_string)
print("python int:",python_int)
print("python float:",python_float)