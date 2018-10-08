for i in range(2,2001):
    values=[]
    for j in range(1,i):
        if i%j == 0:
            values.append(j)
    num=sum(values)
    if num == i:
        print(i)
