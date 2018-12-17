import json
favorite_number=input("What's your favorite number?")
filename="favorite_number.json"
with open(filename,"w") as file_object:#写并存储#
    json.dump(favorite_number,file_object)

with open(filename,"r") as file_object:#读取#
    favorite_number=json.load(file_object)
    print("I know your favorite number! It's"+ favorite_number+".")
