import json
dic={
    '4': 5, 
    '6': 7, 
    '1': 3, 
    '2': 4}
dic1={}
for key,value in sorted(dic.items()):
    dic1[key]=value
with open('sortedkeys.json','w') as f:
    json.dump(dic1,f,indent=6)

print(dic1)