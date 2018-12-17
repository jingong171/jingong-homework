print("Cats contents:")
filename1='cats.txt'
try:
    with open(filename1) as fileobject1:
        contents=fileobject1.read()
        print(contents)
except FileNotFoundError:
    #10-8
    #print("Sorry, there is no such a file.")
    #10-9
    pass

print("\nDogs contents:")
filename2='dogs.txt'
try:
    with open(filename2) as fileobject2:
        contents=fileobject2.read()
        print(contents)
except FileNotFoundError:
    #10-8
    #print("Sorry, there is no such a file.")
    #10-9
    pass

