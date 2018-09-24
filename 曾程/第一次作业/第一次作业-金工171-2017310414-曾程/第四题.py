overall_number=[]
for a in range(1,100):
    overall_number.append(a)#1~99的列表
    
non_prime_number=[]
for i in range(1,100):
    for j in range(2,i):#根据定义，排除掉1和数本身
        if i/j==int(i/j):#找出非素数
            number=i
            non_prime_number.append(number)
            break
prime_number=list(set(overall_number).difference(set(non_prime_number)))
#列表的差集为素数集（差集的方法是百度的）
print(prime_number)
