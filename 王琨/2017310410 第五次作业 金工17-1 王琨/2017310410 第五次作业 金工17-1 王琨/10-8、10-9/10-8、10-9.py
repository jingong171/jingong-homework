filename1='cat.txt'
filename2='dog.txt'

try:
    with open(filename1) as cat_name:
        lines1=cat_name.readlines()
except FileNotFoundError:
    #print("Sorry,the file 'cat.txt' does not exist.")#去除此行第一个‘#’号，程序输出友好提示
    pass#此时程序一言不发
else:
    for line in lines1:
        print(line.rstrip())

        
try:
    with open(filename2) as dog_name:
        lines2=dog_name.readlines()
except FileNotFoundError:
    #print("Sorry,the file 'dog.txt' does not exist.")#去除此行第一个‘#’号，程序输出友好提示
    pass#此时程序一言不发
else:
    for line in lines2:
        print(line.rstrip())
