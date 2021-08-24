import json
datas= [
    {
    "name":"komal",
    
    "score":40,
    "school":"pyds"
},
{
    "name":"koma",
    
    "score":40,
    "school":"pyd"
},
{
    "name":"jaya",
    
    "score":60,
    "school":"pyds"
},
{
    "name":"Sonam",
    "score":60,
    "school":"Union"
},
{
    "name":"Akshit",
    "score":50,
    "school":"Summer Fileld school"
}
]
# python_string=json.loads(datas)
for dict1 in datas:
    for key,value in dict1.items():
        # print(key,value)
        if dict1[key]=='pyds' and dict1['score']>=50:
            print(dict1[key],dict1['score'])


# print(type(python_string))