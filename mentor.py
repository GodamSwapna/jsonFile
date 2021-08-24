import json
list1=[{'id':1,'name':'swapna','collage':11},
        {'id':2,'name':'paru','collage':12},
        {'id':3,'name':'neelu','collage':13,}]
num1=int(input("entre you are index:"))
# print(list1[num1])

for key in list1[num1]:
    # print(key)
    if key=="id":
        id=int(input("enter a id  number:"))
        list1[num1][key]=id
    elif key=="name":
        name=input("enter you are name:")
        list1[num1][key]=name
    elif key=="collage":
        collage=int(input("enter you collage id:"))
        list1[num1][key]=collage
object=json.dumps(list1)  
print(object) 
print(type(object))  
   