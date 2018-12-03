import json
#如果以前存储过最喜爱的数字，就加载它
#否则，就提示用户输入最喜爱的数字并储存它
filename='number.json'
try:
    with open(filename) as f_obj:
        number=json.load(f_obj)
except FileNotFoundError:
    number=input("What's your favorite number?")
    with open(filename,'w') as f_obj:
        json.dump(number,f_obj)
        print("We'll remember your favorite number is "+str(number)+" when you come back!")
else:
    print("I know your favorite number!It's "+str(number)+".")
