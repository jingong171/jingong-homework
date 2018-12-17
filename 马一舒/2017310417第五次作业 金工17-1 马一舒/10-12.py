"""编写一个程序提示用户输入他喜欢的数字"""
import json
filename="number10-12.json"
"""如果有文件就向用户显示它"""
try:
    """从文件中读取值"""
    with open(filename)as file_object:
        digits=json.load(file_object)
        print("I know your favorite number!It's "+str(digits))
except FileNotFoundError:
    """如果没有就输入并储存"""
    while True:
        try:
            number=int(input("请输入你最喜欢的数字："))
            """将这些数字储存到文件中"""
            filename="number.json"
            with open(filename,"w")as file_object:
                json.dump(number,file_object)
                print("I know your favorite number!It's "+str(number))
        except ValueError:
            print("输入错误，请输入数字哦")
        else:
            break

