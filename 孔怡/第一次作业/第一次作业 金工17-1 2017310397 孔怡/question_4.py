list=[]
for i in range(2,100):
    for j in range(2,i):
        if i%j==0:
            break
        else:
            list.append(i)
print(list)
    
