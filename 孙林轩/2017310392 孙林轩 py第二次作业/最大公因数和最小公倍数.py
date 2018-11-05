m=int(input("Please input a number:  "))
n=int(input("Please enter another bigger number:   "))
mn=m*n
rest_num=1
max_num=0
min_num=0
if n%m!=0:
    while rest_num!=0:
        rest_num=n%m
        n=max(m,rest_num)
        m=min(m,rest_num)
    n=max_num
else:
    m=max_num
min_num=(m*n)/max_num
print("最小公倍数是：",min_num)
print("最大公因数是：",max_num)
