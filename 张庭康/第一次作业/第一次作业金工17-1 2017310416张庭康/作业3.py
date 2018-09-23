a=list(range(0,10))
b=list(range(0,10))
c=list(range(1,10))
水仙花数=[]
for x in a:
    for y in b:
        for z in c:
            t=x+y*10+z*100
            if t == x**3+y**3+z**3:
                水仙花数.append(t)
print(水仙花数)
