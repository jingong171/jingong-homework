list=[]
for i in range(1,10):
    for j in range(0,10):
        for k in range(0,10):
            if i*i*i+j*j*j+k*k*k==100*i+10*j+k:
                list.append(100*i+10*j+k)
print(list)
