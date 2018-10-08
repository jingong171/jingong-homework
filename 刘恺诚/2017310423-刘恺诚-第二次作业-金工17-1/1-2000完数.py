for i in range(1,2001):
    su=0;
    for k in range(1,i):
        if i%k==0:
            su=su+k;
    if su==i:
        print(i);
    
