a=[]
b=list(range(1,100))
for x in b:
    c=list(range(2,x))
    for y in c:
        if x%y==0:
            break
    else:
        a.append(x);
print(a);
