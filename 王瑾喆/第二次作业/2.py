GYS=[]
GBS=[]
m=36
n=10
num=[m,n]
for i in range(1,min(num) ):
    if (m%i==0)and (n%i==0):
        GYS.append(i)
print("最大公约数是"+str(max(GYS)))

for k in range(max(num),m*n):
    if (k%m==0) and (k%n==0):
        GBS.append(k)
print("最大公倍数是"+str(min(GBS)))
        
