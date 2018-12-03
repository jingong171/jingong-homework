try:
    a=input('输入第一个数字：')
    b=input('输入第二个数字：')
    a=int(a)
    b=int(b)
except ValueError:
    print('你输入的值不是数字，请重新输入！')
else:
    print('a+b=',str(a+b))
