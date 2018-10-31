all_num=list(range(1,2001))
num=3
perfect_num=[]
for num in all_num:
    k=0
    for i in list(range(1,num)):
        rest=num%i
        if rest==0:
            k=k+i
    if k==num:
        perfect_num.append(num)
print(perfect_num)