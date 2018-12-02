filename1="cats.txt"
filename2="dogs.txt"
print("10-8:")
try:
    with open(filename1) as file_object1:
        print(file_object1.read())
    with open(filename2) as file_object2:
        print(file_object2.read())
except FileNotFoundError:
    print("文件不存在哦~")
print("10-9:")
try:
    with open(filename1) as file_object1:
        print(file_object1.read())
    with open(filename2) as file_object2:
        print(file_object2.read())
except FileNotFoundError:
    pass
