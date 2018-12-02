print('Please enter two number and I will add them.')

judge1=judge2=1
while judge1==1:#while循环使发生错误时可以重新输入
    try:
        number1=int(input('The first number: '))
    except ValueError:
        print('Please enter a number!' )#友好提示
    else:
        judge1=0

while judge2==1:#while循环使发生错误时可以重新输入
    try:
        number2=int(input('The second number:'))
    except ValueError:
        print('Please enter a number!' )#友好提示
    else:
        judge2=0
   
answer=number1+number2
print(str(answer))
