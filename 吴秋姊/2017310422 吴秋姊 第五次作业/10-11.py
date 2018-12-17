import json

#提示用户输入他喜欢的数字
like_number=input("Please enter one of your favorite number: ")

#创造文件
#json.dump接受实参：数据和文件名
filename = "like_number.json"
with open(filename, 'w') as file_object:
    json.dump(like_number, file_object)
#json.load读取
import json

filename = 'like_number.json'
with open(filename) as file_object:
    like_number = json.load(file_object)
    
print("I know your favorite number! It's "+str(like_number)+".")
