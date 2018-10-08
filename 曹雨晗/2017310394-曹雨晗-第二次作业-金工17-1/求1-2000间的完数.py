i=1
for i in range(1,2001):
    j=1
    sum=0
    for j in range(1,i):
        if i%j==0:
            sum=sum+j
    if sum==i:
        print(i)
    
    
