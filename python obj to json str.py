import json
python_dict =  {"name": "David", "age": 6, "class":"I"}
python_list =  ["Red", "Green", "Black"]
python_str =  "Python Json"
python_int =  (1234)
python_float =  (21.34)
python_T =  (True)
python_F =  (False)
python_N =  (None)
python_complex=2+3j

json_dict=json.dumps(python_dict)
json_list=json.dumps(python_list)
json_str=json.dumps(python_str)
json_num1=json.dumps(python_int)
json_num2=json.dumps(python_float)
json_true=json.dumps(python_T)
json_false=json.dumps(python_F)
json_Null=json.dumps(python_N)
json_complex=json.dumps(python_complex)

print("json dict:",json_dict)
print("json list:",json_list)
print("json str:",json_str)
print("json num1:",json_num1)
print("json num2:",json_num2)
print("json false:",json_false)
print("json true:",json_true)
print("json Null:",json_Null)
print("json complex:",json_complex)