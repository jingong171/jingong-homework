import json

#10-11
###提示用户输入一个喜欢的数字
##favorite_number=input("please enter your favorite number:")
##filename='favorite_number.json'
###创建json文件
##with open(filename,'w') as fb:
##    json.dump(favorite_number,fb)
###读取json文件
##with open(filename) as fb1:
##    favorite_number = json.load(fb1)
##    print("I know your favorute number! It is " +str(favorite_number))

#10-12
###提示用户输入一个喜欢的数字
##favorite_number=input("please enter your favorite number:")
##filename='favorite_number.json'
###创建json文件
##with open(filename,'w') as fb:
##    json.dump(favorite_number,fb)
###读取json文件
##with open(filename) as fb1:
##    favorite_number = json.load(fb1)
##    print("I know your favorute number! It is " +str(favorite_number))
try:
    with open('favorite_number.json') as fb1:
        favorite_number = json.load(fb1)
except FileNotFoundError:
    #创新构建json文件
    favorite_number=input("please enter your favorite number:")
    filename='favorite_number.json'
    #创建json文件
    with open(filename,'w') as fb:
        json.dump(favorite_number,fb)
else:
    print("I know your favorute number! It is " +str(favorite_number))
