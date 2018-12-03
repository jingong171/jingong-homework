import json

filename = 'favorite_number.json'

try:
    with open(filename) as file_object:
        number = json.load(file_object)
except FileNotFoundError:
    print("Sorry,the file " + filename + "does not exist.")
else:
    print("I know your favorite number! It's " + str(number))
