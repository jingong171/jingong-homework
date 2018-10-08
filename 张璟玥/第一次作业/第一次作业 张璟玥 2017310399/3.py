numbers=[]
for x in range(100,1000):
    a = (x - x%100)/100  #获取百位数字
    c = (x - 100*a)%10  #获取个位数字
    b = (x - c - a*100)/10  #获取十位数字
    if x == a**3 + b**3 + c**3:
        numbers.append(x)
print(numbers)