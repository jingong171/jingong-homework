#提示用户程序功能
print("您可以输入两个数字，我们将给出这两个数字的和")

#设计循环
while True:
    i=input("请输入您想要相加的数字之一：")
    j=input("请输入您想要相加的另一个数字：")
    try:
        sum = int(i)+int(j)
    except ValueError:
        print("对不起，您输入了文本，还请您重新输入")
    else:
        print(sum)
        break
