a = list(range(0,10))
b = list(range(1,10))
for x in b:
    for y in a:
        for z in a:
            if x**3+y**3+z**3==x*100+y*10+z:
                print(x*100+y*10+z);
