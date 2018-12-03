import json

filename = 'numbers.json'

def get_num():
    numbers = input("What is your favorite number?")
    with open(filename,'w') as f_obj:
        json.dump(numbers,f_obj)

def set_num():
    with open(filename) as f_obj:
        user = json.load(f_obj)
    if user:
        print("I know your favorite number!It's "+user+".")
    else:
        get_num()


get_num()
set_num()
