print("Enter two numbers and I will add them.")
print("Enter 'q' to quit.")

while True:
    first_number=input("\n First number:")
    if first_number=='q':
        break
    second_number=input("\n Second number:")
    if second_number=='q':
        break
    try:
        answer=int(first_number)+int(second_number)
    except ValueError:
        print("The type is not correct.")
    else:
        print(answer)
