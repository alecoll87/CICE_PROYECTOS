import json
import os

absolute_path = os.path.realpath((__file__))
cwd = os.path.dirname(absolute_path)
print(cwd)

'''Jsonize the string '''

# file = open("data.json", encoding="utf8")
# data= file.read()
# print(data)

# data = json.loads(data)
# data["data"][0]["a"] = False
# data = json.dumps(data)
# print(data)
# print(type(data))

'''Jsonize the file'''

# file = open("data.json") #check cwd
# data = json.load(file)
# data["data"][0]["a"] = False
# file.close()
# file = open("data.json", "w")
# json.dump(data, file, indent=4)
# file.close()

with open(f"{cwd}/data.json" , "r", encoding="utf8") as file:
    data = json.load(file)
    print(data)


