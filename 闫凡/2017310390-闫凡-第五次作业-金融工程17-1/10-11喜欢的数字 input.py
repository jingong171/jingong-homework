#导入json模块
import json
#输入数字
favorite_num=input('请输入你喜欢的数字')
filename='favorite_num.json'
#存储数字
with open(filename,'w') as file:
    json.dump(favorite_num,file)
