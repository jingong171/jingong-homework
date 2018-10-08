m=18
n=48
print(str(m)+"与"+str(n))

gongyueshu=[] #公约数列表
for i in range(1,m+1):
    if m%i == 0 and n%i == 0 :
        gongyueshu.append(i)
maxgongyueshu=max(gongyueshu) #求最大公约数
print("最大公约数是："+ str(maxgongyueshu))

gongbeishu=[]
for j in range(n,m*n+1):
    if j%m == 0 and j%n == 0:
        gongbeishu.append(j)
mingongbeishu=min(gongbeishu) #求最小公倍数
print("最小公倍数是：" + str(mingongbeishu))
        

        
