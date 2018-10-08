wanshu=[]
for i in range(1,2001):
    sum=0
    for j in range(1,i):
        if i%j==0:
            sum+=j
    if sum==i:
        wanshu.append(i)
print(wanshu)  
