#给定一个空列表
num=[]

#利用循环法找出符合条件的数
for x in range(1,2001):
    index=[]
    for i in range(1,x):
        if x%i == 0:
            index.append(i)
            y=sum(index)
        #为了保证y 不在中途被输出得到错误答案，需要保证i==x-1后再输出
        if i == x-1:
            if x == y:
                num.append(x)
print("1-2000之间的完数为："+str(num))
