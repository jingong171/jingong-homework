m=5
n=18

if m < n:
    m,n=n,m
x=m
y=n

while m%n!=0:
    z=m%n
    m=n
    n=z

m=x*y/n
print('最大公约数为'+str(n)+','+'最小公倍数为'+str(m)+'。')

