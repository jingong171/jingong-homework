
for i in range(2,2001):
    yinzi=[]
    
    for j in range(1,i):
        
        if i%j==0:
            yinzi.append(j)
    yinzidehe=sum(yinzi)
    
    if yinzidehe==i:
        print(i)
        

