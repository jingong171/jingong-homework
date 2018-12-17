"""友好提醒"""
def file_open(filename):
    """从文件中读取数据"""
    try:
        with open(filename) as file_object:
            contents=file_object.read()
    except FileNotFoundError:
        print("抱歉，未找到"+filename+".")
    else:
        print(contents)
filenames=['cats.txt','dogs.txt']
for filename in filenames:
    file_open(filename)


"""一声不吭"""
def file_open(filename):
    """从文件中读取数据"""
    try:
        with open(filename) as file_object:
            contents=file_object.read()
    except FileNotFoundError:
        pass
    else:
        print(contents)
filenames=['cats.txt','dogs.txt']
for filename in filenames:
    file_open(filename)
