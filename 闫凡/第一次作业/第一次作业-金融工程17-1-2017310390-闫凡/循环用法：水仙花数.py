print("三位数中的水仙花数有：")
for number in range(100,1000):
    a=number%10
    b=(number%100-a)/10
    c=(number-a-b*10)/100
    num=a**3+b**3+c**3
    if num==number:
        print(str(number)+" ")
    

