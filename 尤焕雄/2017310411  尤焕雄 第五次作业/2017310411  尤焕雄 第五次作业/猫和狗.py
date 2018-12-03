file1="cats.txt"
with open(file1,"w") as cat:
    cats_names=["喵喵喵喵喵喵喵","喵喵喵","喵喵喵喵"]
    for i in range(3):
        cat.write(cats_names[i]+"\n")

file2="dogs.txt"
with open(file2,"w") as dog:
    dogs_names=["汪汪汪汪汪汪汪","汪汪汪","汪汪汪汪"]
    for i in range(3):
        dog.write(dogs_names[i]+'\n')
