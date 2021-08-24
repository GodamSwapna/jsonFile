import json
dic={}
list1=[]
index=1
while True:
    user=input("enter user name:")
    password=input("enter user password:")
    dic["user_name"]=user
    dic["password"]=password
    list1.append(dic)
    with open("s.json","a") as f:
        json.dump(dic,f,indent=4)


