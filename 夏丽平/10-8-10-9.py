file_name1 = 'cats.txt'
file_name2 = 'dogs.txt'
#写文件
with open(file_name1,'w') as file_obj:
    file_obj.write('Lucy\n')
    file_obj.write('Lulu\n')
    file_obj.write('Lily\n')
with open(file_name2,'w') as fb:
    fb.write('David\n')
    fb.write('Dam\n')
    fb.write('Dee\n')

#10-8
#读文件
##with open('cats.txt') as file_obj:
##    for line in file_obj:
##        print(line)
##
##with open('dogs.txt') as file_obj:
##    for line in file_obj:
##        print(line)

#代码放置于try之下
try:
    with open('cats.txt') as file_obj:
        for line in file_obj:
            print(line)
except FileNotFoundError:
    print("flie 'cats.txt' doesn't exist.")
try:
    with open('dogs.txt') as file_obj:
        for line in file_obj:
            print(line)
except FileNotFoundError:
    print("flie 'dogs.txt' doesn't exist.")

#10-9
try:
    with open('cats.txt') as file_obj:
        for line in file_obj:
            print(line)
except FileNotFoundError:
    pass
try:
    with open('dogs.txt') as file_obj:
        for line in file_obj:
            print(line)
except FileNotFoundError:
    pass








