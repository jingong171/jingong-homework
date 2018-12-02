import json

filename='number.json'
try:
    with open(filename) as f_obj:   #读取
        number=json.load(f_obj)
except FileNotFoundError:
    favorite_number=int(input("Input your favorite number:\t")) #输入 
    with open(filename,'w') as f_object:    
        json.dump(favorite_number,f_object)
        print("I know your favorite number! It's "+str(favorite_number))
else:
    print("I know your favorite number! It's "+str(number))
