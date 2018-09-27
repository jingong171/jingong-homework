full_integrity=[]#创建完数的空列表
for i in range(1,2001):#遍历1~2000的整数
	factor=[]#创建每个数因子的空列表
	for m in range(1,i):
		if i%m==0:
			factor.append(m)#求出该数字的因子（除自身）
	if i==sum(factor):#完数=因子之和
		full_integrity.append(i)

print(full_integrity)
