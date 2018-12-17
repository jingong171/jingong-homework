import json
filename = 'number.json'
try:
    with open(filename) as file_object:
        number = json.load(file_object)
except FileNotFoundError:
    number = input("Please enter your favorite number: ")
    with open(filename, 'w') as file_object:
        json.dump(number, file_object)
        print("We'll remember your favorite number when you come back, " + "!")
else:     
    print("I know your favorite number!It's "+number+"!")
