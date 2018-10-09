#求m和n的最大公约数和最小公倍数：
m=int(input("请输入第一个整数："))
n=int(input("请输入第二个整数："))
multiply=[]
#比较m、n的大小
bigger=max(m,n)
smaller=min(m,n)
#最大公约数（GCD）：
for factor in range(1,smaller+1):
    if m%factor==0 and n%factor==0:
        GCD=factor
print("m和n的最大公约数是"+str(GCD))
#最小公倍数（LCM）：
for cm in range(bigger,m*n+1):
    if cm%m==0 and cm%n==0:
        multiply.append(cm)
LCM=min(multiply)
print("m和n的最小公倍数是"+str(LCM))
