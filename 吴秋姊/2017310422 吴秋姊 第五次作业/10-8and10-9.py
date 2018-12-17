#创建新文件
filename1="cats.txt"

try:
    with open(filename1) as file_object1:
        contents =  file_object1.read()
except FileNotFoundError:
##10-8要求
##    msg = "Sorry, the file " + filename1 + " does not exist."
##    print(msg)
    pass
else:
    print(contents)

#创建新文件
filename2="dogs.txt"

try:
    with open(filename2) as file_object2:
        contents =  file_object2.read()
except FileNotFoundError:
##10-8要求
##    msg = "Sorry, the file " + filename2 + " does not exist."
    pass
##    print(msg)
else:
    print(contents)
