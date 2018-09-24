for k in range(100,1000):
    a=k//100
    b=(k-a*100)//10
    c=k-a*100-b*10
    if k==a**3+b**3+c**3:
        print(k)
