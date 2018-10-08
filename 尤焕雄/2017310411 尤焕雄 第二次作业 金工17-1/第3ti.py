for i in range(2,2000):
    sum=0
    for j in range (1,i):
        if i%j==0:
            sum=sum+j
    if i==sum:
        print(i)
    
            
