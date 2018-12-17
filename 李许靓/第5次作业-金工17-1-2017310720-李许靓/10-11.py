#favorite_number_write.py
import json
favoritenum=input("enter your favorite number:")
filename='favoritenum.json'
with open(filename,'w') as fileobj:
    json.dump(favoritenum,fileobj)

#favorite_number_read.py
try:
    with open('favoritenum.json') as fileobj:
        num=json.load(fileobj)
        print("I know your favorite number! It's " + str(num) + ".")
except FileNotFoundError:
    print("sorry ,I don't konw your favorite number.")