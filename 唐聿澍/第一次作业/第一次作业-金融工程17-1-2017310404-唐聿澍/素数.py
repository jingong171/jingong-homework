for n in range(2,100):
    a = 2
    while (n%a) != 0 :
        a += 1
    if a == n :
        print("素数是：" + str(a) + ".\n")
