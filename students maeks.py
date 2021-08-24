import json
user=int(input("How many student passed in exams:"))
i=1
dict1={}
while i<=user:
    name=input("enter student name here:")
    marks=int(input("scoring marks in exam with in 100:"))
    dict1[name]=marks
    i+=1
with open("students_mark.json","w") as f:
    json.dump(dict1,f,indent=4)
print(dict1)