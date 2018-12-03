import json

with open('likehood.json','r')as obj:
    number=json.load(obj)
    print("I know your favourite number!It's "+str(number))
    
