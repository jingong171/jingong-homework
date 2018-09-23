for i in range(100,1000):
    fir=i%10
    sec=(i//10)%10
    thr=i//100
    while (fir**3+sec**3+thr**3==i):
        print(i)
        i+=1
        


    

