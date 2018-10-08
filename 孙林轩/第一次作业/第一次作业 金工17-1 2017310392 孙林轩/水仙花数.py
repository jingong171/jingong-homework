all_num=list(range(0,10))
num=0
target=[]
for a in all_num:
    for b in all_num:
        for c in all_num:
            num=100*a+10*b+c
            if num==a**3+b**3+c**3 and 99<num<1000:
                target.append(num)
print(target)