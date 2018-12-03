import json
def get_newNum():
    num=input("请输入你喜欢的数字：")
    filename = 'num.json'
    with open(filename,'w') as obj:
        json.dump(num,obj)
    return num
def get_stored_num():
    filename = 'num.json'
    try:
        with open(filename) as obj:
            num = json.load(obj)
    except FileNotFoundError:
        return None
    else:
        return num
def show_num():
    num=get_stored_num()
    if num:
        print("I know your favourite number!.It is "+num+"!")
    else:
        num=get_newNum()
show_num()
    
