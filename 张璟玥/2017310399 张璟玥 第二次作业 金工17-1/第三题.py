
perfectnumbers=[]
for i in range(1,1000):
    factors=[]
    for a in range    (1,i):
        if i%a==0:
            factors.append(a)
            if i==sum(factors):
                perfectnumbers.append(i)
print(perfectnumbers)
