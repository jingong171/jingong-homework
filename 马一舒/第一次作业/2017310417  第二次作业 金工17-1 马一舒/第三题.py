for m in range(1,2001):
    M=[]
    for n in range (1,m):
        if m % n == 0 :
            M.append(n)
    if sum(M)== m :
        print(m)
        
