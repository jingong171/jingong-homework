print("Give me two numbers, and I'll add them.")

while True:
    first_number=input("\nFirst number:")
    second_number=input("\nSecond number:")
    try:
        answer=int(first_number)+int(second_number)
    except ValueError:
        print("You can't add text!")
    else:
        print(answer)
        

    
