import csv
import matplotlib.pyplot as plt

#导入显示中文的库
from pylab import mpl  
mpl.rcParams['font.sans-serif'] = ['SimHei']


#ids存储学号，names1存储名字，class存储班级，sign_num签到次数
ids_1=[]
ids_2=[]
ids_3=[]

names1=[]
names2=[]
names3=[]

class_1=[]
class_2=[]
class_3=[]

sign_num=[]

filenames=['pythonsign_20181009.csv','pythonsign_20181030.csv','pythonsign_20181113.csv']

#把csv文件写入对应的列表中
with open(filenames[0]) as f:

    reader=csv.reader(f)
    header_row=next(reader)
    for row in reader:
        names1.append(row[1])
        ids_1.append(row[0])
        class_1.append(row[3])
        
#每次签到次数都加1
num=1


for i in range(1,len(names1)+1):
    sign_num.append(num)


with open(filenames[1]) as f:

    reader=csv.reader(f)
    header_row=next(reader)
    for row in reader:
        names2.append(row[1])
        ids_2.append(row[0])
        class_2.append(row[3])

with open(filenames[2]) as f:

    reader=csv.reader(f)
    header_row=next(reader)
    for row in reader:
        names3.append(row[1])
        ids_3.append(row[0])
        class_3.append(row[3])

#定义一个返回列表的元素的指定值索引的函数
def return_index(name,names1):
    """返回列表中指定值的索引"""
    
    for a in range(len(names1)):
        if names1[a]==name:
            return a

for student in names2:
    

    if student in names1:
        index=return_index(student,names1)
        sign_num[index]+=1

    else:
        names1.append(student)
        index=return_index(student,names2)
        ids_1.append(ids_2[index])
        class_1.append(class_2[index])
        sign_num.append(num)
        

for student in names3:
    if student in names1:
        index=return_index(student,names1)
        sign_num[index]+=1
    else:
        names1.append(student)
        index=return_index(student,names3)
        ids_1.append(ids_3[index])
        class_1.append(class_3[index])
        sign_num.append(num)


#制作散点图
plt.scatter(names1,sign_num,edgecolor='none',c='blue',s=10)
plt.title('签到次数散点图',fontsize=18)
plt.xlabel('姓名',fontsize=18)
plt.ylabel('签到次数',fontsize=18)

plt.tick_params(axis='both',which='major',labelsize=8)

plt.show()

#保存为txt文件
filename1='签到信息表.txt'
with open(filename1,'w') as file_object:
    for i in range(len(names1)):
        file_object.write('姓名: '+names1[i])
        file_object.write('  学号: '+str(ids_1[i]))
        file_object.write('  班级: '+class_1[i])
        file_object.write('  签到次数: '+str(sign_num[i])+'\n')


