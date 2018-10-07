for i in range(2,2001):
    p=[]
    n=-1
    w=i
    for j in range(1,i):
        if i%j==0:
            n=n+1
            w=w-j
            p.append(j)
    if w==0:
        print(i)
            
            
        
            
        
