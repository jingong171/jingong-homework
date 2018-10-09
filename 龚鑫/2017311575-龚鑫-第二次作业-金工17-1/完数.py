
for number in range(1,2001):
    sum1=0
    for another_number in range(1,number):
        if number%another_number==0:
            sum1+=another_number
    if number==sum1:
        print(number)
