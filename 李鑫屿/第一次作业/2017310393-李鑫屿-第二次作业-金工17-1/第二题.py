n=10
m=8
if n>m:
    a=m
if n<m:
    a=n
for b in range(1,a+1):
    if (n%b==0)and(m%b==0):
        c=b
print(c)
z=m*n
if(m>n):
    a=m
if(m<n):
    a=n
for i in range(a,z+1):
    if (i%n==0)and(i%m==0):
        break
print(i)

    
