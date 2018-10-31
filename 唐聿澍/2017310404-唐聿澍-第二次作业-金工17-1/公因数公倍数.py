

m = int(input("输入正整数一："))#m、n输入正整数
n = int(input("输入正整数二："))

if m >= n :#判别m、n大小关系，确定变量i、j
    i = n
    j = m
else:
    i = m
    j = n

while m % i != 0 or n % i != 0 :#判别是否能整除，下同
    i -= 1
print("两者最大公因数是：" + str(i))

while j % m != 0 or j % n != 0:
    j += 1
print("两者最小公倍数是：" + str(j))
