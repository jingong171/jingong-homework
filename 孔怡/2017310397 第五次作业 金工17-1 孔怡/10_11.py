import json

number=input('Please input your favourite number: ')

filename='number.json'
with open(filename,'w') as f_obj:
    json.dump(number,f_obj)
    print("I know your favorite number! It's "+number+"!")
