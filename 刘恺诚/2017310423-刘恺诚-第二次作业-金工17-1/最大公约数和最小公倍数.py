m=int(input('m='));
n=int(input('n='));

maxgys=1;  #最大公约数
for i in range(1,min(m,n)+1):
    if (m%i==0)and (n%i==0):
        maxgys=i;

mingbs=(m/maxgys)*(n/maxgys)*maxgys;


print("最大公约数是",maxgys);
print("最小公倍数是",int(mingbs));        
