m=int(input("输入第一个数m:"))
n=int(input("输入第二个数n:"))
i=max(m,n)
j=min(m,n)
a=1
b=1
c=1
d=1
if i%j==0:
    #判断他们是否能整除
    print(i)
    print(j)
else:
    while a!=0 or b!=0:
        i=i+1
        a=i%m
        b=i%n
    print(i)
    #i为最大公倍数
    while c!=0 or d!=0:
        j=j-1
        c=m%j
        d=n%j
    print(j)
    #j为最大公约数
    
