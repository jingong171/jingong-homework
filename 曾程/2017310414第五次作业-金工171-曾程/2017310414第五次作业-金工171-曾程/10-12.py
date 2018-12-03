import json

def get_stored_favorite_number():
    """如果存储了数字，就获取它"""
    filename='favorite_number.json'
    try:
        with open(filename) as f_obj:
            favorite_number=json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return favorite_number

def get_new_favorite_number():
    """没有存储数字，就存储新的数字"""
    favorite_number=input("What's your favorite number? ")
    filename='favorite_number.json'
    with open(filename,'w') as f_obj:
        json.dump(favorite_number,f_obj)
    return favorite_number
        
def show_favorite_number():
    favorite_number=get_stored_favorite_number()
    if favorite_number:
        print("I know your favorite number! It's "+favorite_number+".")
    else:
        favorite_number=get_new_favorite_number()
        print("I'll show you your favorite number next time!")

show_favorite_number()
