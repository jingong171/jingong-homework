print("下列是1-2000之前所有的完数：")
for i  in range(1,2001):
    sum=0
    for k in range(1,i):
        if i%k==0:
            sum=sum+k
    if sum==i:
        print(i)
