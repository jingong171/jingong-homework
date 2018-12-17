# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 19:02:24 2018

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
    pass