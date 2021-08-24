import json
# data='''Name Abhishek
#  Designation CEO of navgurukul
#  Gender male
#  Age 21'''
# with open("text.txt","w") as f:
#     f.write(data)
with open("text.txt","r") as f:
    dic={}
    for data in f:
        info=data.split()
        i=0
        str1=""
        while i<len(info):
            if info[i]!=info[0]:
                str1=str1+" "+info[i]
            dic[info[0]]=str1
            i+=1
    with open("myinfo.json","w") as f1:
        json.dump(dic,f1,indent=6)
