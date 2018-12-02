import json#json安装

fNum=input("What's your favorite number? ")#输入数字

filename='number.json'

with open(filename,'w') as objW:#打开json写入
    json.dump(fNum,objW)

with open(filename,'r') as objR:#打开json读取
    fNumOut=json.load(objR)

print("I know your favorite number! It's " + fNumOut )#打印数字
