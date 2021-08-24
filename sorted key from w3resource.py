import json
j_str = {'4': 5, '6': 7, '1': 3, '2': 4}
sorted_json=json.dumps(j_str,sort_keys=True,indent=4)
print(sorted_json)
print(type(sorted_json))
