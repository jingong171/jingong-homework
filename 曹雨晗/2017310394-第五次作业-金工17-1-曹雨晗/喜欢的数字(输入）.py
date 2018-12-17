import json

number = input('Please enter your favorite number:')

filename='favorite_number.json'
try:
    with open(filename, 'w') as file_object:
        json.dump(number, file_object)
except FileNotFoundError:
    print("Sorry, the file " + filename + "does not exist.")
