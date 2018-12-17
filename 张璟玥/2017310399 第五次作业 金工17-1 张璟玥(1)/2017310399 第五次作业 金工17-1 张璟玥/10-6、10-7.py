print("Give me two numbers,and I'll add them up.")
print("Enter 'q' to quit.")
import json
while True:
    first_number=input('\nFirst number:')
    if first_number=='q':
        break
    second_number=input('\nSecond number:')
    if second_number=='q':
        break
    try:
        answer= int(first_number)+int(second_number)
    except ValueError:
        print('Please enter numbers!')
    else:
        print(answer)
        filename='answer.json'
        with open(filename,'w') as f_obj:
            json.dump(answer,f_obj)

