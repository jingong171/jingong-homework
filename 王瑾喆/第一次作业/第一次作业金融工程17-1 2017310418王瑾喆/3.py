for a in range(100,1000):
    gewei=a%10
    shiwei=int((a%100-gewei)/10)
    baiwei=int(a/100)
    if a==gewei**3+shiwei**3+baiwei**3:
        print(a)
