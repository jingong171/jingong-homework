filename1='cats.txt'
filename2='dogs.txt'
try:
    with open(filename1) as f_obj1:
        with open(filename2) as f_obj2:
            cats=f_obj1.read()
            dogs=f_obj2.read()
            print(cats+"\n"+dogs)
except FileNotFoundError:
    print('不存在')
    print("---snip---")
