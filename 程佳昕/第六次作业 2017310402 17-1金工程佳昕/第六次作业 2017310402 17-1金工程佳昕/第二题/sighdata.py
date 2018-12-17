#导入各种需要的模块和工具
import csv 
import matplotlib.pyplot as plt  
from pylab import mpl   
#创造多个列表来储存三个csv文件中的不同类型数据 
stu_num1=[] 
stu_num2=[] 
stu_num3=[] 
names1=[] 
names2=[] 
names3=[] 
class_num1=[] 
class_num2=[] 
class_num3=[] 
sign_num=[] 
#定义需打开文件名
filenames=['pythonsign_20181009.csv','pythonsign_20181030.csv','pythonsign_20181113.csv']  
with open(filenames[0]) as f: 
    reader=csv.reader(f)  
    header_row=next(reader) 
    for row in reader: 
        names1.append(row[1]) 
        stu_num1.append(row[0]) 
        class_num1.append(row[3]) 
p=1 
#把第一个文件里所有姓名对应的签到数加上1 
for i in range(1,len(names1)+1):  
    sign_num.append(p) 
with open(filenames[1]) as f:  
    reader=csv.reader(f) 
    header_row=next(reader) 
    for row in reader: 
        names2.append(row[1]) 
        stu_num2.append(row[0]) 
        class_num2.append(row[3]) 
with open(filenames[2]) as f: 
    reader=csv.reader(f) 
    header_row=next(reader) 
    for row in reader: 
        names3.append(row[1]) 
        stu_num3.append(row[0]) 
        class_num3.append(row[3]) 
#定义一个返回列表的元素的指定值索引的函数 
def return_index(name,names1): 
    """返回列表中指定值的索引"""
    for a in range(len(names1)): 
        if names1[a]==name: 
            return a  
for student in names2: 
#找到第一个文件中已经出现过的同学对应的签到数据加1 
    if student in names1: 
        index=return_index(student,names1) 
        sign_num[index]+=1 
#如果第一个csv文件中没有这个同学，就把这个同学的姓名，学号，班级加到列表之后，然后定义这个姓名对应的签到次数为1 
    else: 
        names1.append(student) 
        index=return_index(student,names2) 
        stu_num1.append(stu_num2[index]) 
        class_num1.append(class_num2[index]) 
        sign_num.append(p) 
#对第三个csv文件进行同样的操作 
for student in names3: 
    if student in names1: 
        index=return_index(student,names1) 
        sign_num[index]+=1 
    else: 
        names1.append(student) 
        index=return_index(student,names3) 
        stu_num1.append(stu_num3[index]) 
        class_num1.append(class_num3[index]) 
        sign_num.append(p) 
#用matplotlib做图 
plt.scatter(names1,sign_num,c='red',s=8) 
plt.title('the times of attending python class',fontsize=24) 
plt.xlabel('students names',fontsize=14) 
plt.ylabel('times of attending',fontsize=14) 
plt.tick_params(axis='both',which='major',labelsize=6) 
plt.show() 
#保存文件 
filename1='files of attending' 
with open(filename1,'w') as file_object: 
    for i in range(len(names1)): 
        file_object.write('name: '+names1[i]) 
        file_object.write('school ID: '+str(stu_num1[i])) 
        file_object.write('class: '+class_num1[i]) 
        file_object.write('attendence times: '+str(sign_num[i])+'\n') 
