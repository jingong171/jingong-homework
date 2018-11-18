for m in range(100,999):
    a=m//100
    c=m%10
    b=(m-a*100-c)/10
    if m==a**3+b**3+c**3:
        print(m)
