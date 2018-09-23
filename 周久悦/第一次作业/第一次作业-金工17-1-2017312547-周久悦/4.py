list_1 = list(range(2,101))
for i in list_1:
    flag=1
    k=i**(1/2)
    if k>=2:
        list_2=list(range(2,int(k)+1))
        for j in list_2:
            if i%j==0:
                flag=0
                break
    if flag==1:
        print(i)
