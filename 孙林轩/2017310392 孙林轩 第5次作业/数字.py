import json
F_number=[]
#用来建立存储到文件中的列表
def Getnewnumber():
    """获得新数字"""
    try:
        num=int(input("Please tell me your favorite number: "))
    except ValueError:
        print("You can only enter a number!")
    else:
        return num
def ReadNowNumbers():
    """读出现在文件中的数字列表"""
    try:
        with open("C:/Users/孙林轩/PycharmProjects/Hello world（temp）/Favorite numbers.txt") as F:
            numbers=json.load(F)
    except FileNotFoundError:
        print("I have lost my files!")
    else:
        return numbers
def RememberNumbers(num):
    """将现在用户输入的数字写入文件"""
    try:
        with open("C:/Users/孙林轩/PycharmProjects/Hello world（temp）/Favorite numbers.txt","w") as F:
            F_number.append(num)
            json.dump(F_number,F)
    except FileNotFoundError:
        print("I have lost my files!")
def main():
    num=Getnewnumber()
    numbers=ReadNowNumbers()
    if num in numbers:
        print("Now I remember, your favorite number is:",num)
    else:
        print("I will remember it!")
    RememberNumbers(num)
main()