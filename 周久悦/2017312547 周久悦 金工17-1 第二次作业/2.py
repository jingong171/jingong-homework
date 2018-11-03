m=180;n=160
if m==n:
    gcd=lcm=m #gcd:最大公约数，lcm:最小公倍数
elif m>n:
    for x in list(range(n,0,-1)):
        if (m%x==0)&(n%x==0)==1:
            gcd=x
            lcm=m*n/gcd
            break
else:
    for t in list(range(m,0,-1)):
        if (m%t==0)&(n%t==0)==1:
            gcd=t
            lcm=m*n/gcd
            break
print("最大公约数是"+str(gcd)+"，最小公倍数是"+str(lcm)+"。")
