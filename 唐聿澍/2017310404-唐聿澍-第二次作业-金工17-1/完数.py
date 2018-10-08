s = 0 #s是和函数
print("1到2000的完数有：" + "\n")
for m in range(1,2001):#1-2000找m
    i = m
    while i > 0 :
        k = m % i #判断是否是因数
        if k == 0 :
            s = s + i #求和因数
        i -= 1
    if m == s - m : #判断是否是完数
        print(m)
    s = 0 #重新s赋值为0
