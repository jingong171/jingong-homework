m=16
n=24
digits_1=[]
digits_2=[]
#枚举求m的因子
for i in range(1,m):
    if m%i==0:
        digits_1.append(i)
#枚举求n的因子
for j in range(1,n):
    if n%j==0:
        digits_2.append(j)
digits_3=[]
for i in digits_1:
    for j in digits_2:
        if i==j:
            digits_3.append(i)#将公共的因子放入空列表3中
a=max(digits_3)
b=m*n/a
message_1="m和n最大公约数: "+str(a)
message_2="m和n最小公倍数: "+str(b)
print(message_1)
print(message_2)
