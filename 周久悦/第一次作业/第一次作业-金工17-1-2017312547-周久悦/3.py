list = list(range(100,1000))
for i in list:
    m=i%10
    n=((i-m)%100)/10
    p=(i-10*n-m)/100
    if i==m**3+n**3+p**3:
        print(i)
