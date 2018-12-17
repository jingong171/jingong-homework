def read_names(filename):
    try:
        with open(filename) as f_obj:
            #读取内容
            contents=f_obj.read()
    except FileNotFoundError:
        #输出友好消息：
        #msg="The file "+filename+" does not exist."
        #print(msg)
        #一言不发：
        pass
    else:
        #正常时打印内容
        print(contents)

filenames=['cats_names.txt','dogs_names.txt']
for filename in filenames:
    read_names(filename)