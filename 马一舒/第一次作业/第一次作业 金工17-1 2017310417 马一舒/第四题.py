digits=[]
for n in range(2,101):
    count=0
    for i in range (2,n+1):
        if n %i != 0:
            count=count+1
    if count==n-2:
        digits.append(n)
print(digits)
