import json

filename = 'numbers.json'

try:
    with open(filename) as f_obj:
        numbers = json.load(f_obj)
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)
else:
    print("I konw your favorite number,it's:" + numbers + "!")

