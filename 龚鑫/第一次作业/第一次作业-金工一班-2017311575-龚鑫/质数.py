list1=[]
list2=[]
for i in list(range(2,100)):
    for k in list(range(2,i)):
        if i%k==0:
            list1.append(i)

for m in list(range(2,100)):
    if m not in list1:
        list2.append(m)

print(list2)
