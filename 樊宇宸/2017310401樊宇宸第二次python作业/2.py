#输入两个正整数m,n
m=int(input())
n=int(input())
#将m,n赋值给a,b
a=m
b=n
#对a,b进行辗转相除求的最大公约数p
while(a!=0)and(b!=0):
    if a>b:
      a=a%b
    else:
      b=b%a
if a==0:
    p=b
else:
    p=a
print(p)
#p是m,n的最大公约数，那么显然m/p,n/p是m,n的互质的因数，三者相乘必为最小公倍数
print(int(p*(m/p)*(n/p)))

        

    
