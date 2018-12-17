#10—8
print('cats&dogs')
def animal_names(filename):
    
    """打印文件储存的动物名"""

    #捕捉FileNotFound'错误并打印友好的信息
    try:
        with open(filename) as file_obj:
            contents=file_obj.read()
            print(contents+'\n')
    except FileNotFoundError:
        message="没有找到"+filename
        print(message)

filenames=['cats.txt','dogs.txt']
for filename in filenames:
    animal_names(filename)

    
#10—9
print('silent cats&dogs')
def animal_names(filename):
    
    """打印文件中储存的动物名"""

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
