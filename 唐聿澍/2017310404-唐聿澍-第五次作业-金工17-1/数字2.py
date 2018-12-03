import json#json安装
filename='number_2.json'

try:
    with open(filename)as obj:#打开json
        number=json.load(obj)#读取数字
except FileNotFoundError:#错误抓取
    number=input("What's your favorite number? ")
    with open(filename,'w')as obj:#打开json写入
        json.dump(number,obj)
        print("Now I know "+ number + " is your favorite number.")#未写入时打印
else:
    print('Your favorite number is '+ number +' !')#已写入时打印
