import json
json_obj =  '{ "Name":"David", "Class":"I", "Age":6 }'
pyth_str=json.loads(json_obj)
print(pyth_str)
print(pyth_str['Name'])
print(pyth_str['Class'])
print(pyth_str['Age'])


pyth_dict =  { "Name":"David", "Class":"I", "Age":6 }
json_str= json.dumps(pyth_dict)
print(type(json_str))