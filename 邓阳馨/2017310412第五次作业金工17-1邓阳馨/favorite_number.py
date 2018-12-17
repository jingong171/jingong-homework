import json

number=input("please enter your favorite number:")

filename='number.json'
with open(filename,'w')as file_object:
    json.dump(number, file_object)
