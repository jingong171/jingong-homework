filename_cat = 'cat.txt'
filename_dog = 'dog.txt'

#10-8 猫和狗

try:
    with open(filename_cat) as file_object:
        names = file_object.read()
except FileNotFoundError:
    print('The file' + filename_cat + 'does not exist.')
else:
    print("Cats' names are:" + names)

try:
    with open(filename_dog) as file_object:
        names = file_object.read()
except FileNotFoundError:
    print('The file' + filename_dog + 'does not exist.')
else:
    print("Dogs' names are:" + names)


#10-9 沉默的猫和狗

try:
    with open(filename_cat) as file_object:
        names = file_object.read()
except FileNotFoundError:
    pass
else:
    print(names)

try:
    with open(filename_dog) as file_object:
        names = file_object.read()
except FileNotFoundError:
    pass
else:
    print(names)
