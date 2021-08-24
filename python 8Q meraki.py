import json
list1=[["neelam","programer","24","2400"],
["komal","trainer","24","20000"],
["anuradha","HR","25","40000"],
["Abhishek","manager","29","63000"]  ]
i=0
dic1={}
while i<len(list1):
    j=0
    dic2={}
    while j<len(list1[i]):
        if list1[i][j]==list1[i][0]:
            dic2['name']=list1[i][j]
        elif list1[i][j]==list1[i][1]:
            dic2['desgnation']=list1[i][j]
        elif list1[i][j]==list1[i][2]:
            dic2['Age']=list1[i][j]
        elif list1[i][j]==list1[i][3]:
            dic2['Salary']=list1[i][j]
        j+=1
        str1='emp'+str(i+1)
    dic1[str1]=dic2
    i+=1
with open("employee.json","w+") as f:
    json.dump(dic1,f,indent=4)
# print(dic1)
# print(type(dic1))