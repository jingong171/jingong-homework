import csv

#Get student number,name,class,number of sign.
filename1='pythonsign_20181009.csv'
filename2='pythonsign_20181030.csv'
filename3='pythonsign_20181113.csv'
filenames=[filename1,filename2,filename3]

#把三个文件里的班级，姓名，学号先取出。
names=[],numbers=[],Classes=[],signs=[]
for filename in filenames:
    with open(filename) as f:
        reader=csv.reader(f)
        for row in reader:
            number=row[0]
            name=row[1]
            Class=row[3]
            names.append(name)
            numbers.append(number)
            Classes.append(Class)

##运用一个函数来通过姓名出现次数统计签到次数：
for name in names:
    i=names.count(name)
    sings.append(i)
#创建字典去除列表中重复数据
New_names=set(names)
New_numbers=set(numbers)
New_Classes=set(Classes)
information=[New_names,New_numbers,New_Classes,signs]
print(signs)

#画散点图：
import matplotlib.pyplot as plt
x_values=New_names
y_values=sings

plt.scatter(x_values,y_values,s=200)

plt.title("Student's Check-in times",fontsize=24)
plt.xlabel("value",fontsize=14)
pil.ylabel("Check-in times",fontsize=14)

plt.tick_params(axi='both',which='major',labelsize=14)
plt.show()






##with open(filename2) as f2:
##    reader2=csv.reader(f2)
##    for row in reader2:
##        name=row[1]
##        names.append(name)
##
##with open(filename3) as f3:
##    reader3=csv.reader(f3)
##    for row in reader3:
##        name=row[1]
##        names.append(name)
##print(names)
####name_all=[names1,names2,names3]
####name_valid=[]
####for name in names:
####    i=names.count(name)
####print(i)
####    

