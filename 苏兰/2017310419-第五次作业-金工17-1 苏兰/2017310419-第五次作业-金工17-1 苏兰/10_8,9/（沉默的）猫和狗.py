#10.8
print('猫和狗')
def animal_names(filename):
    """打印一个文件中储存的动物的名字"""

    #捕捉FileNotFound'错误并打印友好的信息
    try:
        with open(filename) as file_obj:
            contents=file_obj.read()
            print(contents+'\n')
    except FileNotFoundError:
        msg="对不起，未找到"+filename
        print(msg)

filenames=['cats.txt','dogs.txt']
for filename in filenames:
    animal_names(filename)

    
#10.9
print('沉默的猫和狗')
def animal_names(filename):
    """打印一个文件中储存的动物的名字"""

    #捕捉FileNotFound'错误，当错误出现时直接跳过该文件
    try:
        with open(filename) as file_obj:
            contents=file_obj.read()
            print(contents+'\n')
    except FileNotFoundError:
        pass

filenames=['cats.txt','dogs.txt']
for filename in filenames:
    animal_names(filename)
