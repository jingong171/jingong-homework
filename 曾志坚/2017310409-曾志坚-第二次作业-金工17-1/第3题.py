perfect_numbers = []

for n in range(1,2001) :
    sum = 0
    for divisor in range(1,n) :
        if n%divisor == 0 :
            sum = sum + divisor
    if n == sum :
        perfect_numbers.append(n)

print(perfect_numbers)
