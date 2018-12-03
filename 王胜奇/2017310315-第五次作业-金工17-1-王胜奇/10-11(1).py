num=input("你喜欢的数字是：")
    filename = 'numbers.json'    
    num=int(num)
    with open(filename,"w") as f_obj:
        json.dump(num,f_obj)