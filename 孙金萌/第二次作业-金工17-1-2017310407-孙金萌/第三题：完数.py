n = []
for i in range(1,2000):
    m = []
    for j in range(1,i):
        if i%j==0:
            m.append(j)
    num = sum(m)
    if num==i:
        n.append(i)
print(n)
        
