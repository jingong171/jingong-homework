num=[];
for m in range(2,100):
    for n in range(2,m):
        if (m%n==0):
            break
    else:
        num.append(m)
print(num)
