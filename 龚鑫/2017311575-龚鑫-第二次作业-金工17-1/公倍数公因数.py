m=eval(input("请输入一个数："))
n=eval(input("请输入另一个数："))
list1=[]
list2=[]
for number in range(1,m+n):
    if m%number==0 and n%number==0:
        list1.append(number)
for number in range(1,m*n):
    if number%m==0 and number%n==0:
        list2.append(number)
print("最小公倍数是{}，最大公因数是{}".format(list2[-1],list1[-1]))
