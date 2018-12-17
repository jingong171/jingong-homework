try:
    #读取猫文件
    file1="cats.txt"
    with open(file1) as cat:
        cats=cat.readlines()

    ##读取狗文件
    file2="dogs.txt"
    with open(file2) as dog:
        dogs=dog.readlines()
except FileNotFoundError:
##    pass   10
    print("这个文件找不到哦")
else:
    ##把猫狗打印出来
    for i in range(3):
        print(cats[i])

    for j in range(3):
        print(dogs[j])
