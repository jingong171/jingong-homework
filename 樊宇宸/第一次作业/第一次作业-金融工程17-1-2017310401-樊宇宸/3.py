for i in range(100,1000):
    a=(i%10)
    b=((i-a)/10)%10
    c=(i-b*10-a)/100
    if i==(a**3+b**3+c**3):
        print(i)
