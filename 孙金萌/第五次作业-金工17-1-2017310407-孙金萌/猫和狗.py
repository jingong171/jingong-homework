filename1 = 'cat.txt'
filename2 = 'dog.txt'

try:
    with open(filename1) as f1_object:
        f1 = f1_object.read()
    with open(filename2) as f2_object:
        f2 = f2_object.read()
except FileNotFoundError:
    print("Not aligned,the file does not exist.")
else:
    print(f1)
    print(f2)


##filename1 = 'cat.txt'
##filename2 = 'dog.txt'
##
##try:
##    with open(filename1) as f1_object:
##        f1 = f1_object.read()
##    with open(filename2) as f2_object:
##        f2 = f2_object.read()
##except FileNotFoundError:
##    pass
##else:
##    print(f1)
##    print(f2)
