m=255
n=99
t=1
for i in range(1,10):
    if (m%i==0 and n%i==0):
        m=m/i
        n=n/i
        t=t*i
print(t)
    
    
