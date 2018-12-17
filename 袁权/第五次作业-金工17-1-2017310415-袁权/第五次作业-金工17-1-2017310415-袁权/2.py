filename1='dogs.txt'
filename2='cats.txt'

try:
    with open(filename1)as f_obj1:
        content1=f_obj1.read()
    with open(filename2)as f_obj2:
        content2=f_obj2.read()
except FileNotFoundError:
    msg="未找到该文件！"
    print(msg)
else:
    print(content1)
    print(content2)
    


