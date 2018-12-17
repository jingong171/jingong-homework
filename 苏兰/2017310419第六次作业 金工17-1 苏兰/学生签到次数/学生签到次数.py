import csv
import matplotlib.pyplot as plt
from pylab import mpl   
mpl.rcParams['font.sans-serif'] = ['SimHei'] 
# Get ID, name, class,and times from file.

filename1 = 'pythonsign_20181009.csv'
filename2='pythonsign_20181030.csv'
filename3='pythonsign_20181113.csv'
#定义签到次数列表
times=[]
#将三个csv文件的信息写入三个列表中
with open(filename1) as f1:
    reader1 = csv.reader(f1)
    header_row=next(reader1) 
    IDs1,names1,classes1=[],[],[]
    for row in reader1:
        IDs1.append(row[0])
        names1.append(row[1])
        classes1.append(row[3])
##设置签到变化值为1
num=1
##第一个文件写入完成后，把第一个文件中出现的同学的签到次数设为1 
for i in range(1,len(names1)+1):  
    times.append(num)
    
with open(filename2) as f2:
    reader2 = csv.reader(f2)
    header_row=next(reader2) 
    IDs2,names2,classes2=[],[],[]
    for row in reader2:
        IDs2.append(row[0])
        names2.append(row[1])
        classes2.append(row[3])

with open(filename3) as f3:
    reader3 = csv.reader(f3)
    header_row=next(reader3) 
    IDs3,names3,classes3=[],[],[]
    for row in reader3:
        IDs3.append(row[0])
        names3.append(row[1])
        classes3.append(row[3])
#定义一个返回列表的元素的指定值索引的函数
def return_index(name,names1): 
    """返回列表中指定值的索引"""
    for a in range(len(names1)): 
        if names1[a]==name: 
            return a
#如果第二个文件中出现了第一个文件中签到的同学的名字，则给此同学的签到次数加1
for student in names2: 
    if student in names1: 
        index=return_index(student,names1) 
        times[index]+=1 
    #如果第一个csv文件中没有这个同学，就把这个同学的姓名，学号，班级通过索引查找添加并且把这个同学的签到次数设为1 
    else: 
        names1.append(student) 
        index=return_index(student,names2) 
        IDs1.append(IDs2[index]) 
        classes1.append(classes2[index]) 
        times.append(num) 
#对第三个csv文件同理
for student in names3: 
    if student in names1: 
        index=return_index(student,names1) 
        times[index]+=1 
    else: 
        names1.append(student) 
        index=return_index(student,names3) 
        IDs1.append(IDs3[index]) 
        classes1.append(classes3[index]) 
        times.append(num) 
#画散点图 
plt.scatter(names1,times,edgecolor='none',c='gray',s=10) 
plt.title('签到次数散点图',fontsize=20) 
plt.xlabel('姓名',fontsize=20) 
plt.ylabel('签到次数',fontsize=20) 
plt.tick_params(axis='both',which='major',labelsize=8) 
#显示图 
plt.show() 
#保存签到次数文件 
filename1='签到次数' 
with open(filename1,'w') as file_object: 
    for i in range(len(names1)): 
        file_object.write('姓名: '+names1[i]) 
        file_object.write(' 学号: '+str(IDs1[i])) 
        file_object.write(' 班级: '+classes1[i]) 
        file_object.write(' 签到次数: '+str(times[i])+'\n') 




