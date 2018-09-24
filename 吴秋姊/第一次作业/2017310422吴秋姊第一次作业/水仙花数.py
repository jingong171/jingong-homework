for i in range(100,1000):
    x=int(i/100)
    y=int((i/10)-x*10)
    z=int(i-x*100-y*10)
    if i==x**3+y**3+z**3:
        print(i)
