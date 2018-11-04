m=27
n=18
numbers=[]
for i in range(2,n):
    if m%i ==0:
        if n%i==0:
            numbers.append(i)
x=max(numbers)
print('最大公因数是')
print(x)
y=m*n/x
print('最小公倍数是')
print(y)
    
