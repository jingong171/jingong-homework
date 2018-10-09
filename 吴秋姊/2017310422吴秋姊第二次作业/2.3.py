for i in range(1,1001):
    sum=0;
    for j in range(1,i):    
        if i%j==0:
            sum=sum+j;
        else:
            j=j+1;
    if sum==i:
        print(j);
    else:
        i=i+1;
