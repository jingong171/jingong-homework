for i in range(1,2001):
    k=0   #k是因数和
    #找出所有因数并叠加
    for j in range(1,i):
        if i%j==0:
            k=k+j
    #检验完数        
    if i==k:
        print(i)
