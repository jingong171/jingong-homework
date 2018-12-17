import csv
import matplotlib.pyplot as plt
from pylab import mpl  
mpl.rcParams['font.sans-serif'] = ['SimHei']

#存储学号
stu_num1=[]
stu_num2=[]
stu_num3=[]
#存储名字
names1=[]
names2=[]
names3=[]
#存储班级
class1=[]
class2=[]
class3=[]
#签到次数
sign_num=[]

#打开文件
filenames=['pythonsign_20181009.csv','pythonsign_20181030.csv','pythonsign_20181113.csv']

#把第一个csv文件的信息写入第一个文件对应的列表中
with open(filenames[0]) as f:

    reader=csv.reader(f)
    header_row=next(reader)
    for row in reader:
        names1.append(row[1])
        stu_num1.append(row[0])
        class1.append(row[3])
        
#num表示每次签到增加的值
num=1

#第一个文件写入完成后，把第一个文件中出现的同学的签到次数设为1
for i in range(1,len(names1)+1):
    sign_num.append(num)

#把第二个csv文件的信息写入第二个文件对应的列表中
with open(filenames[1]) as f:

    reader=csv.reader(f)
    header_row=next(reader)
    for row in reader:
        names2.append(row[1])
        stu_num2.append(row[0])
        class2.append(row[3])

#把第三个csv文件的信息写入第三个文件对应的列表中
with open(filenames[2]) as f:

    reader=csv.reader(f)
    header_row=next(reader)
    for row in reader:
        names3.append(row[1])
        stu_num3.append(row[0])
        class3.append(row[3])

#定义一个返回列表的元素的指定值索引的函数
def return_index(name,names1):
    """返回列表中指定值的索引"""
    
    for a in range(len(names1)):
        if names1[a]==name:
            return a

#将第二个csv文件写入后的数据，与第一个csv文件写入后的数据进行比较
for student in names2:
    
#如果第一个csv文件中有这个同学，找到他的签到数据，签到次数加1
    if student in names1:
        index=return_index(student,names1)
        sign_num[index]+=1
#如果没有,签到次数为1
    else:
        names1.append(student)
        index=return_index(student,names2)
        stu_num1.append(stu_num2[index])
        class1.append(class2[index])
        sign_num.append(num)
        
#对第三个csv文件进行同样的操作
for student in names3:
    if student in names1:
        index=return_index(student,names1)
        sign_num[index]+=1
    else:
        names1.append(student)
        index=return_index(student,names3)
        stu_num1.append(stu_num3[index])
        class1.append(class3[index])
        sign_num.append(num)


#用数据画散点图
plt.scatter(names1,sign_num,edgecolor='none',c='blue',s=10)
plt.title('同学签到次数散点图',fontsize=25)
plt.xlabel('学生姓名',fontsize=18)
plt.ylabel('签到次数',fontsize=18)

plt.tick_params(axis='both',which='major',labelsize=8)


plt.show()

plt.savefig('同学签到次数散点图.png')

#保存为签到次数文件
filename1='签到次数文件'
with open(filename1,'w') as file_object:
    for i in range(len(names1)):
        file_object.write('姓名: '+names1[i])
        file_object.write('  学号: '+str(stu_num1[i]))
        file_object.write('  班级: '+class1[i])
        file_object.write('  签到次数: '+str(sign_num[i])+'\n')
