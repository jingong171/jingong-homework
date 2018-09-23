for a in range(1,10):
    for b in range(1,10):
        for c in range(1,10):
            d=a**3+b**3+c**3
            e=100*a+10*b+c
            if d==e:
                print(d)
