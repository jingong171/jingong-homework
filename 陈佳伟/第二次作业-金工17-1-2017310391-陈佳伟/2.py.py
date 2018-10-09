
m=15
n=20
x=1
for i in range(1,16):
    if m%i==0 and n%i==0:
        x=x*i

print( '最大公约数：'+str(x))
print( '最小公倍数：'+str(m*n/x))     
                        

                        
