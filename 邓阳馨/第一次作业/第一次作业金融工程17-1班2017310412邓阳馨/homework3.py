for d3 in range(1,10):
    for d2 in range(0,10):
        for d1 in range(0,10):
            if d3*100+d2*10+d1==d3**3+d2**3+d1**3:
                print(d3*100+d2*10+d1)
