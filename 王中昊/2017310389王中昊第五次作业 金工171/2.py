filename_1='cats.txt'
filename_2='dogs.txt'
try:
    with open(filename_1) as obj_1:
        contents_1=obj_1.read()
    with open(filename_2) as obj_2:
        contents_2=obj_2.read()
except FileNotFoundError:
    pass

    
