import json
while True:
    try:
        with open('likehood.json','r')as obj:
            number=json.load(obj)
            print("I know your favourite number!It's "+str(number))
            break
    except Exception:
        number=int(input("请输入一个你喜欢的数字"))

        filename='likehood.json'
        with open(filename,'w') as obj:
            json.dump(number,obj)
        

