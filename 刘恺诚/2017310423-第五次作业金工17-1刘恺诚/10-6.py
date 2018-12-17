a=input("请输入第一个数");
b=input("请输入第二个数")

try:
    sum=float(a)+float(b);
except ValueError:
    print("ValueError:请输入两个数字")


print("两数之和为"+str(sum))
