def read_text(filename):
    try:
        with open(filename) as f_obj:
            contents=f_obj.read()
    except FileNotFoundError:
        pass
    else:
        print(contents)
animal_list=["cats.txt","dogs.txt"]
for animal in animal_list:
    read_text(animal)
