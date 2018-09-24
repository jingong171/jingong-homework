number=[]
for x in range(2,100):
    for y in range(2,x):
        if x%y==0:
            break
        else:
            number.append(x)
print(x)