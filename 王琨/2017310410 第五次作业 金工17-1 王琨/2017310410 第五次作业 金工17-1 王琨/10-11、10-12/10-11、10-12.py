import json

filename='UserFavouriteNumber'
try:
    with open(filename) as used:
        number=json.load(used)
except FileNotFoundError:
    number=input('Please enter your favorite number:' )
    with open(filename,'w') as Number:
        json.dump(number,Number)
else:
    print('I know youe favourite number!It`s '+number)
