num1=45
num2=54#定义两个数字
num=[num1,num2]#创建一个两个数字的列表
for i in range(1,min(num)+1):#遍历由1到两个数字中较小的数字
    if (num1%i==0)and(num2%i==0):#公约数是除两数余数都为0
        GCD=i#GCD的赋值会被不断覆盖，最终取得最大公约数
        LCM=int((num1*num2)/GCD)#最小公倍数=两数相乘除以最大公约数

print("这两个数字的最大公约数是"+str(GCD))
print("这两个数字的最小公倍数是"+str(LCM))
