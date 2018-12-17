import json

filename='number.json'
try:
    with open(filename) as f_obj:
        number=json.load(f_obj)
except FileNotFoundError:
    number=input("What's your favourite number? ")
    with open(filename,'w') as f_obj:
        json.dump(number,f_obj)
        print("We have remembered your favourite number! It's "+number+".")
else:
    print("Your favourite number is "+number+"!")
