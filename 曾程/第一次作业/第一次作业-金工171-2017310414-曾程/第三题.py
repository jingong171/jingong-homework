Narcissistic_number=[]
for a in range(1,10):
    for b in range(0,10):
        for c in range(0,10):
            if a*100+b*10+c==a**3+b**3+c**3:
                number=a*100+b*10+c
                Narcissistic_number.append(number)
                continue
print(Narcissistic_number)
