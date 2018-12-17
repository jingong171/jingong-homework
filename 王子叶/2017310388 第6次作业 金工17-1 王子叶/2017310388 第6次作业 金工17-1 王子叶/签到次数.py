import csv
#从文件中Get 学号，班级，姓名#
filename="pythonsign_20181009.csv"
with open(filename) as f1:
    reader=csv.reader(f1)
    header_row=next(reader)
    print(header_row)
filename="pythonsign_20181030.csv"
with open(filename) as f2:
    reader=csv.reader(f2)
    header_row=next(reader)
    print(header_row)
filename="pythonsign_20181113.csv"
with open(filename) as f3:
    reader=csvrader(f3)
    header_row=next(reader)
    print(header_row)
with open(filename,"w")as file_object:
    file_object.write(header_row)#读取三个文件信息
ID number=[]
for row in reader:
    ID number=int(row[1])
    ID numbers.append(ID number)
for value in range(1,4):
    frequency=ID number.count(value)
    frequencies.append(frequency)
hist.title="The frequncies of students atteding class"
hist.x_title="ID number"
hist.x_labels=[ID number]
hist.y_title="frequency of stuednts attending class"
hist.add（frequencies)
hist.render_to_file("dice_visual.svg")



