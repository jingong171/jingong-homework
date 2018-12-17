import json

filename='favorite_Num.json'
try:
    with open(filename) as f_obj:
        favorite_num=f_obj.read()
        print("I know your favorite number!It's "+favorite_num+".")
except FileNotFoundError:
    print("You haven't enter your favorite number.")
    favorite_num=input("Please enter：")

    filename='favorite_Num.json'

    with open(filename,'w') as f_obj:
        json.dump(favorite_num,f_obj)
    print("I know your favorite number!It's "+favorite_num+".")

