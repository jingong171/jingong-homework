"""编写一个程序提示用户输入他喜欢的数字"""
import json
while True:
    try:
        number=int(input("请输入你最喜欢的数字："))
        """将这些数字储存到文件中"""
        filename="number.json"
        with open(filename,"w")as file_object:
            json.dump(number,file_object)
            """从文件中读取值"""
        with open(filename)as file_object:
            digits=json.load(file_object)
            print("I know your favorite number!It's "+str(digits))

    except ValueError:
        print("输入错误，请输入数字哦")

    else:
        break
