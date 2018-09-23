numbers=list(range(100,1000))
for number in numbers:
    a=number//100
    b=(number-100*a)//10
    c=number-100*a-10*b
    if number==a**3+b**3+c**3:
        print(number)
