list=[2]


for i in range(2,100):
    for j in range(2,100):
        t=i*j
        if (t<100):
            list.append(t)
for k in range(2,100):
    if k not in list:
        print(k,' ')

        
        
