#尝试打开文件
files=['cats.txt','dogs.txt']
#使用for循环读取文件
for file in files:
    try:
        with open(file) as file:
            file_read=file.read()
        print(file_read.title())
#处理文件不存在的错误
    except FileNotFoundError:
#输出提示信息
        print('文件'+str(file)+'不存在')
