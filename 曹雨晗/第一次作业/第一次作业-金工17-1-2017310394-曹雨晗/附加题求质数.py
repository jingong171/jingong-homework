requested_numbers=[]
i = 1
for i in range(1,101):
    m = 0
    j = 1
    for j in range(1,i+1):
        k = i%j
        if(k == 0):
            m = m+1
    if m == 2:
        requested_numbers.append(i)
print(requested_numbers)
    
