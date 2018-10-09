#先建立一个用于储存完数的空列表
perfects=[]
for perfect in range(1,2001):
    #对于每一个数，先让adds为零
    adds=0
    for div in range(1,perfect):
        #adds为1至perfect-1的数中所有因数的和
        if perfect%div==0:
            adds=adds+div
    #找到一个完数后在完数的列表中加上一个数
    if perfect==adds:
        perfects.append(perfect)
#输出完数列表
print(perfects)
