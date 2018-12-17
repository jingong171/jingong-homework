import json
while True:
    try:
        m=int(input("请输入你最喜欢的数字"))
        """m为该用户最喜欢的数字"""
        filename="10-11.json"
        with open(filename,"w") as file_object:
            json.dump(m,file_object)
        with open(filename) as file_object:
            numbers=json.load(file_object)
        print("I know your favorite number! It's "+str(numbers))
        break
    except ValueError:
        print("你输入的不是数字哦~请重新输入")
    
