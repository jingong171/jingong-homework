#用户输入m,n的值
m=int(input("m:"))
n=int(input("n:"))
#用于存储所有除一以外的公因数
mindis=[]
for mindi in range(1,max(m,n)):
    if m%mindi==0 and n%mindi==0:
        mindis.append(mindi)
#输出最后一个找到的公因数
print("最大公约数是："+str(mindis[-1]))

for minmul in range(max(m,n),m*n+1):
    if minmul%m==0 and minmul%n==0:
        print("最小公倍数是："+str(minmul))
        break
#找到第一个公倍数时结束循环
