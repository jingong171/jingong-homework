# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 19:02:59 2018

@author: WSQ
"""
import json
while True:
    try:
        num=input("你喜欢的数字是：")
        filename = 'numbers.json'    
        num=int(num)
        with open(filename,"w") as f_obj:
            json.dump(num,f_obj)
        filename = 'numbers.json'
        with open(filename,) as f_obj:
            number=json.load(f_obj)
        print("I know your favorite number! It's"++str(num))
    except ValueError:
        print("请输入你喜欢的数字")
