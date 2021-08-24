import json
my_info='''{ 
            "Name":"Swapna",
            "Age":21,
            "Qualification":"BSc",
            "Contact_num" : 6301898297,
            "Gender":"Female",
            "marital_status":"faslse"
        }'''
# with open("swapna.json","r") as f:
object=json.loads(my_info)
print(object)
# print(type(x))
# print(type(python_dict))
# with open("myfile1.json","w") as f:
#     json.dump(my_info,f,indent=4)

