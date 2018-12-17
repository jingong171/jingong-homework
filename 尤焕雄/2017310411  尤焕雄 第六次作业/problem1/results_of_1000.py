from Die import die
#一个六面一个十面的骰子
d1=die()
d2=die(10)
results=[]
#生成结果和频率两个列表
frequency=[]
elements=set([x*y for x in range(1,7) for y in range(1,11)])
##列表中元素已按顺序排列



##生成结果
for i in range(1,1001):
    results.append((d1.roll())*(d2.roll()))

##计算每个结果的频数
for ele in elements:
    f=results.count(ele)
    frequency.append(f)



