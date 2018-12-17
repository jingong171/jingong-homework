import json
try:
    with open('favoritenum.json') as fileobj:
        num=json.load(fileobj)
except FileNotFoundError:
    favoritenum=input("enter your favorite number:")
    filename='favoritenum.json'
    with open(filename,'w') as fileobj:
        json.dump(favoritenum,fileobj)
    with open('favoritenum.json') as fileobj:
        num=json.load(fileobj)
        print("I know your favorite number! It's " + str(num) + ".")
else:
    print("I know your favorite number! It's " + str(num) + ".")