import json


def get_stored_number():
    """如果存储了数字， 就获取它"""
    filename = 'favorite_number.json'
    try:
        with open(filename) as file_obj:
            num = json.load(file_obj)
    except FileNotFoundError:
        return None
    else:
        return num


def get_new_number():
    """提示用户输入他喜欢的数字，并用json.dump()存到favorite_number.json"""
    filename = 'favorite_number.json'
    while True:
        num = input('输入你喜欢的数字:')
        try:
            num = int(num)
        except ValueError:
            print('请确保输入的是整数')
        else:
            break
    with open(filename, 'w') as file_obj:
        json.dump(num, file_obj)
    return num


def greet_user():
    num = get_stored_number()
    if num:
        print("欢迎再次读取你最喜欢的数字："+str(num))
    else:
        num = get_new_number()
        print("我们会记住你最喜欢的数字："+str(num))


greet_user()
