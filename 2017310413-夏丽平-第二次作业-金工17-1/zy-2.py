#规定两个数
m=45
n=25
k=0
f=0
#寻找m,n的最大公约数
for i in range(1,max(m,n)+1):
    if m%i==0 and n%i==0:
        k=i
#求m,n的最小公倍数
f=m*n/k
#打印最小公倍数
print(f)
