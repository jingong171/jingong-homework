for m in list(range(1,2001)):
    sum=0
    for x in list(range(1,m)):
        if m%x==0:
            sum=sum+x #因子和
    if sum==m:
        print(str(m)+"是一个完数。")
