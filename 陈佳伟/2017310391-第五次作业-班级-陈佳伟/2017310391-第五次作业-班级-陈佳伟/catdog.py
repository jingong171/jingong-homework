try:
    with open('C:\Users\HP\Desktop\py\cats.txt') as cats:
        for line1 in cats:
            print(line1.strip())
    with open('C:\Users\HP\Desktop\py\dogs.txt') as dogs:
        for line2 in dogs:
            print(line2.strip())
except FileNotFoundError:
    print('抱歉，文件找不到。')
