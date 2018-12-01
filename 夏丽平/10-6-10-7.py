print("Give me two number,and I will add them")
print("enter 'q' to quit")

##10-6

##number1=input("\nenter the first number:")
##try:
##    number1=int(number1)
##except ValueError:
##    print("sorry,you didn't enter a number")
##number2=input("\nenter the second number:")
##try:
##    number2=int(number2)
##except ValueError:
##    print("sorry,you didn't enter a number")
##answer=number1+number2
##print("the answer is "+str(answer))

##10-7 
flag = True
while flag:
    number1=input("\nenter the first number:")
    if number1 == 'q':
        break
    try:
        number1=int(number1)
    except ValueError:
        print("sorry,you didn't enter a number")
        continue
    number2=input("\nenter the first number:")
    if number2 == 'q':
        break
    try:
        number2=int(number2)
    except ValueError:
        print("sorry,you didn't enter a number")
        continue
    answer = number1 + number2
    print(answer)
    
