#打印所有三位的水仙花数
     #在数论中，水仙花数（Narcissistic number）也称为自恋数、自幂数或阿姆斯特朗数（Armstrong number）是指一N位数，其各个数之N次方和等于该数。例如：153是三位水仙花数, 有 153 = 1^3 + 5^3 + 3^3. 
     #(来源: 维基百科 水仙花数)

for a in range(1,10):
    for b in range(0,10):
        for c in range(0,10):
            if a**3 + b**3 + c**3 == a*100 + b*10 +c:
                print(a**3 + b**3 + c**3)