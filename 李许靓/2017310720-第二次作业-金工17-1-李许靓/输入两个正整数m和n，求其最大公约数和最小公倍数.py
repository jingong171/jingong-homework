num1=20
num2=100
if num1<num2:
    num0=num1
    num1=num2
    num2=num0
a=num1
b=num2
while b!=0:
    num0=a%b
    a=b
    b=num0
print("最大公约数为"+str(a))
print("最小公倍数为"+str(num1*num2/a))
