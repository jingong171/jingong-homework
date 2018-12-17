filename1='cats.txt'
filename2='dogs.txt'

try:
    with open(filename1) as file_object1:
        lines1=file_object1.readlines()   
    for line1 in lines1:
        print('猫的名字是：'+line1+'\n')
        
    with open(filename2) as file_object2:
        lines2=file_object2.readlines()   
    for line2 in lines2:
        print('狗的名字是：'+line2+'\n')

except FileNotFoundError:
    print('无法找到文件。')
