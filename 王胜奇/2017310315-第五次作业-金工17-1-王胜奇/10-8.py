# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 18:46:37 2018

@author: WSQ
"""
try:
    with open('cat.txt') as file_object:
        contents = file_object.read()
        print(contents.rstrip())
    with open('dog.txt') as file_object:
        contents = file_object.read()
        print(contents.rstrip())
except FileNotFoundError:
    print("请找到文件")
