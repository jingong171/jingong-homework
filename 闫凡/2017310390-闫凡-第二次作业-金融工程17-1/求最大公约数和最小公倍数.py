m=58
n=123
nums=list(range(1,124))
nums.reverse()
for num in nums:
    if m%num==0 and n%num==0:
        print(str(m)+"和"+str(n)+"的最大公约数是"+str(num))
        break
nums=list(range(n,n*m+1))
for num in nums:
    if num%m==0 and num%n==0:
        print(str(m)+"和"+str(n)+"的最小公倍数是"+str(num))
        break
