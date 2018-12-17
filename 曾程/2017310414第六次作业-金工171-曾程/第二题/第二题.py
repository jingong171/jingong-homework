import csv
import matplotlib.pyplot as plt
file1='pythonsign_20181009.csv'
file2='pythonsign_20181030.csv'
file3='pythonsign_20181113.csv'

students=[] #建立一个学生信息列表，用于存储学号、姓名和班级信息

with open(file1) as f1:
    reader=csv.reader(f1)
    header_row=next(reader)
    
    for row in reader:
        student=[row[0],row[1],row[3],1]
        #分别指文件中的学号、姓名、班级，以及新添加签到信息（每次签到会更改这个量）
        students.append(student)

with open(file2) as f2:
    reader=csv.reader(f2)
    header_row=next(reader)
    
    for row in reader: #遍历新签到表所有学生信息
        flag=False #作为标记
        for i in range(0,len(students)-1): #遍历students列表中所有信息，用于匹配
            if students[i][0]==row[0] or row[1]==students[i][1]:
                students[i][3]+=1 #新表中出现与旧表相同名字/学号，签到次数加一
                flag=True #退出遍历students列表，开始匹配下一位同学
                continue
        if flag==False:
            student=[row[0],row[1],row[3],1] #新出现的同学信息
            students.append(student)

with open(file3) as f3:
    reader=csv.reader(f3)
    header_row=next(reader)
    
    for row in reader:
        flag=False
        for i in range(0,len(students)-1):
            if students[i][0]==row[0] or row[1]==students[i][1]:
                students[i][3]+=1
                flag=True
                continue
        if flag==False:
            student=[row[0],row[1],row[3],1]
            students.append(student)

namelist=[] #学生姓名汇总表，作为可视化视图的横坐标
times=[] #签到次数汇总表，作为可视化视图的纵坐标
for i in range(0,len(students)-1):
    namelist.append(students[i][1]) #将姓名信息添加进namelist列表
    times.append(students[i][3]) #将签到次数信息添加进times列表

plt.scatter(namelist,times,c='blue',s=10)
plt.title("Python Signs",fontsize=24)
plt.xlabel("Student names",fontsize=14)
plt.ylabel("Times",fontsize=14)
plt.tick_params(axis='x',labelsize=4)
plt.show()
