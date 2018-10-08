m=10
n=5
if m==n:
    print("最大公因数是"+m)
    print("最小公倍数是"+m)
else:
    son1=[]
    son2=[]
    son=[]
    for i in range(1,m+1):
        if m%i==0:
            son1.append(i)
    for j in range(1,n+1):
        if n%j==0:
            son2.append(j)
    for i in son1:
        for j in son2:
            if i==j:
                son.append(i)
    l=son[-1]
    k=m*n/son[-1]
    print("最大公倍数是"+str(l))
    print("最小公倍数是"+str(k))
            
