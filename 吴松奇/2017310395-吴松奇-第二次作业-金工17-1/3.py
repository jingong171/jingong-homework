numbers=list(range(1,2001))
for number in numbers:
    a=1
    b=0
    while a<number:
        if number%a==0:
            b=a+b
            #b为所有因子之和
        a=a+1
        #a为所有可能是该数因子的数
    if number==b:
        #判断该数是否等于所有因子之和
        print(number)
        
        
