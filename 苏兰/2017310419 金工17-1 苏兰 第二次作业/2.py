#任意给定两个正整数，并创建两个空列表
m=836
n=58
num1=[]
num2=[]

#利用循环法找到最大公约数
for i in range(1,n+1):
    if m%i == 0 and n%i == 0:
	    num1.append(i)
x=max(num1)
print("836和58的最大公约数是："+str(x))

#同理利用循环法找出最小公倍数
for u in range(1,m*n):
    if u%m == 0 and u%n == 0:
        num2.append(u)
y=min(num2)
print("836和58的最小公倍数是："+str(y))
