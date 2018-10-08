m=12
n=8
i=1
j=1
M=[]
for i in range(1,m+1):
    if m%i==0:
        M.append(i)
for i in range(1,n+1):
    if n%i==0:
        if i in M:
            if j>=i:
                j=j
            else:
                j=i
print("m和n的最大公约数为：" + str(j))
M2=[]
k=m*n
for i in range(1,m*n):
    if i%m==0:
        M2.append(i)
for i in range(1,m*n):
    if i%n==0:
        if i in M2:
            if k<=i:
                k=k
            else:
                k=i
print("m和n的最小公倍数为：" + str(k))
