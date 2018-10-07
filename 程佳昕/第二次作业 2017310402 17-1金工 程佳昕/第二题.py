m=int(input("请输入第一个数字m"))
n=int(input("请输入第二个数字n"))
s=m*n
while m!=n:
    if m>n:
        m=m-n
    elif m<n:
        n=n-m
else:
    print("最大公因数为"+str(m))
    print("最小公倍数为"+str(s/m))

