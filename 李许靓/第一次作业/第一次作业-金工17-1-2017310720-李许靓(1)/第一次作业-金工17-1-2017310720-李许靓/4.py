list=[ ]
for i in range(2,101):
    k=2
    sum=0
    while k<i:
        if i%k==0:
            sum=sum+1
        k=k+1
    if sum==0:
        list.append(i)
print(list)
