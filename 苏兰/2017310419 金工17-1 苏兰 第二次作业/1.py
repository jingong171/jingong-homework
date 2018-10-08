#创建一个空列表
index=[]

#利用循环找到题目中相加的数并添加至空列表
for x in range(1,11):
    x=(3*x)**2
    index.append(x)

#利用sum函数求和
y=sum(index)
print("所求式的值为： "+str(y))
