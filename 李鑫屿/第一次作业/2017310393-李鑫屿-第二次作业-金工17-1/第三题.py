for i in range(1,2001):
    sum=0
    for a in range(1,i):
        if (i%a==0):
            sum+=a
    if (i==sum):
        print(i)
        

    
    
