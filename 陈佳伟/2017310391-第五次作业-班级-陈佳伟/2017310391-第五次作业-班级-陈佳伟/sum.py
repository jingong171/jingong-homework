##while True的意义在于可以一直循环
while True:
    a=input('输入一个数：')
    b=input('在输入一个数：')
    try:
        a=int(a)
        b=int(b)
    except ValueError:
        print('\n\n抱歉，请输入数字')
    else:
        print('\t\t'+str(a)+'+'+str(b)+'='+str(a+b)+'\n')
    
