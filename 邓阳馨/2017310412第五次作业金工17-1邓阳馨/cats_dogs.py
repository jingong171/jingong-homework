
def show_names(filename):
    """show the name in txt"""
    try:
        with open(filename)as file_object:
            contents=file_object.read()
    except FileNotFoundError:
        msg = "Sorry, the file " + filename + " does not exist."
        print(msg)
    else:
        print(filename+"\n"+contents)

##沉默的猫和狗
##def show_names(filename):
##    """show the name in txt"""
##    try:
##        with open(filename)as file_object:
##            contens=file_object.read()
##    except FileNotFoundError:
##        pass
##    else:
##        print(contents)

        
filenames=['cats.txt','dogs.txt']
for filename in filenames:
    show_names(filename)

