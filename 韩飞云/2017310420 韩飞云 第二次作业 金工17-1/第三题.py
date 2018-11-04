shu=list(range(1,2001))
wanshu=[]
for x in shu:
    he=0
    yinzi=list(range(1,x))
    for y in yinzi:
        if x%y == 0:
            he = he+y
    if x == he:
        wanshu.append(x)
print('完数有:')
print(wanshu)
        
