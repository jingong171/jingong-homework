for num in range(100,1000):
    g = num % 10
    b = int(num/100)
    s = int((num-b*100)/10)
    sum = g*g*g+b*b*b+s*s*s
    if sum == num:
        print(num)
