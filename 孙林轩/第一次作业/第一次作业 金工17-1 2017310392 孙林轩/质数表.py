all_num=list(range(2,100))
i=2
for i in range(2,11):
    for num in all_num[i:]:
        rest=num%i
        if rest==0:
            all_num.remove(num)
print(all_num)