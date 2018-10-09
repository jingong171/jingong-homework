for number in range(2, 1000):
    factors = [] 
    for yinzi in range(1,number):
        if number%yinzi == 0:
            factors.append(yinzi)
    if sum(factors) == number:
        print(str(number)+' ')
