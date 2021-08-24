import json
dic={"string":"swapna","number":21,"float":7.2,"list":[1,2,3],"dict":{'1':'a','2':'b'},"complex":3+5j}
x=json.dumps(dic)
print(x)
