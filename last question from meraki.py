import json
dic={
    "shopping_list":
        { 
            "chaco":"15",
            "Biscuits":"50",
            "Diary_milk":"30",
            "ice_cream":"20",
        } 
}
user=input("which item do you want:")
num=int(input("enter how many items do you want:"))
for dic1 in dic:
    # print(dic[dic1])
    # for key in dic[dic1]:
        # print(key)
    if user in dic[dic1]:
        dic[dic1][user]=num
    elif user not in dic[dic1]: 
        dic[dic1][user]=num
with open("shopping.json","w") as f:
    json.dump(dic,f,indent=4)
# print(dic)