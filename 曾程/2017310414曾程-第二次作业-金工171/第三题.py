perfect_number=[]
for i in range(1,2000):
    factor=[]
    for j in range(1,i):
        if i%j==0:
            factor.append(j)
        continue
    sum_num=0
    for k in factor:
        sum_num +=k
    if i==sum_num:
        perfect_number.append(i)
print(perfect_number)
    
