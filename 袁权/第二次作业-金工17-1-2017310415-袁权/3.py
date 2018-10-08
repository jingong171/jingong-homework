i=1
list=[]
for i in range(1,2000):
    j=1
    for j in range(1,i):
        if (i%j==0):
            list.append(list)
    s=0
    for k in range(list):
        s=s+k
    if(s==i-1):
        print(i)

            
        
            
        
