factor=[]
for pernum in range(5,2001):
    for b in range(1,pernum):
        if pernum%b==0:
            factor.append(b)
    if sum(factor)==pernum:
        print(pernum)
        print(factor)
    factor=[]
#其中pernum表示完数，factor表示完数的因子
