#10-8
file1='cats.txt'  #读取文件'cats.txt'
try:
    with open(file1) as file1_obj:
        contents1=file1_obj.read()
except FileNotFoundError:
    print("The file "+file1+" is not found.")  #提示文件不存在
else:
    print(contents1)

#10-9
file2='dogs.txt'  #读取文件'dogs.txt'
try:
    with open(file2) as file2_obj:
        contents2=file2_obj.read()
except FileNotFoundError:
    pass  #文件不存在时一言不发
else:
    print(contents2)
