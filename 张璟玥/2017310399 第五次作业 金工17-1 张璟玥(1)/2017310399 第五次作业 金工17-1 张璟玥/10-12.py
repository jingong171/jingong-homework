import json
filename='favorite_number.json'
try:
    with open(filename) as f_obj:
        favorite_number=json.load(f_obj)
#如果没有存储数字，就输入并存储它
except FileNotFoundError:
    favorite_number=input("What's your favorite number?")
    with open(filename,'w') as f_obj:
        json.dump(favorite_number,f_obj)
        print("I know your favorite number now!It's "+favorite_number+".")
#如果以前存储了数字
else:
    print("I know your favorite number!It's "+favorite_number+".")
