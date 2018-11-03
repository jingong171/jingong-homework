m = 25
n = 15
if m<=n:
    s=m
else:
    s=n
for i in range(1,s+1):
    if ((m%i==0)&(n%i==0)):
        h=i
        f=m*n/h
print(str(m)+"和"+str(n)+"的最大公约数和最小公倍数分别为"+str(h)+","+str(f))
