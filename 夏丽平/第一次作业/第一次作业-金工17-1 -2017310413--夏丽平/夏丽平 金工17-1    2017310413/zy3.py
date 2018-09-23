for a in range(1,10):
    for b in range(0,9):
        for c in range(0,9):
            i=a*100+b*10+c
            if a*100+b*10+c==a**3+b**3+c**3:
                print(i)
