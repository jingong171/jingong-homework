#求N=100之前的所有素数，将其存放于一个列表中并打印之。(选做，可加分，单次作业最大分100)
#一般解法
list=[];
for x in range(2,1000):
	for y in range(2,x):
		if x%y==0:
			break
	else:
		list.append(x)
print(list)