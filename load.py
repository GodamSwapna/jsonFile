import json
with open("myfile.json","r") as f:
    x=json.load(f)
    print(type(x))
    print(x)