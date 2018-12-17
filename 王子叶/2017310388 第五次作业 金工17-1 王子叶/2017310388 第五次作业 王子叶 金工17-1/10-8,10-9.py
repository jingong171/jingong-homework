filenames=["cats.txt","dogs.txt"]
for filename in filenames:
    try:
        with open(filename) as file_object:#open 和读取txt文件#
            contents=file_object.read()
    except FileNotFoundError: 
        pass #10-9的要求，按照10-8的要求是打印友好错误消息print("The document is not exist")#
    else:
        print(contents)
