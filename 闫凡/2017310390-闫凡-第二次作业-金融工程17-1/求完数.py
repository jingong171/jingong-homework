numbers=[]
for num in range(1,2001):
    list1=list(range(1,num))
    factors=[]
    for num1 in list1:
        if num%num1==0:
            factors.append(num1)
    if sum(factors)==num:
        numbers.append(num)
print(numbers)

