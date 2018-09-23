for i in list(range(1,999)):
    k=i%10
    j=(i//10)%10
    l=i//100
    if i==k**3+j**3+l**3:
        print (i)
