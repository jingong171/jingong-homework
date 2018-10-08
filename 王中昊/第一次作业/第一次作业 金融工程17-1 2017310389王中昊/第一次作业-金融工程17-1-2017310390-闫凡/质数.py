list=[]
b=0
for num in range(1,100):
    for i in range(2,num):
        a=num%i
        if a==0:
            b=1
            break
        else:
            b=0
    if b==0:
        list.append(num)        
print(list)
            
