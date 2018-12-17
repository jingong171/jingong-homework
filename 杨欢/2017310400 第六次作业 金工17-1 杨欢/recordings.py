import csv
import pygal
import matplotlib.pyplot as plt

#arrived记录所有出现过的学号，不论是否重复
arrived=[]
#students列表内的元素均为字典，记录每位学生的学号。姓名、班级信息
students=[]
#numbers记录所有签到过的学生的学号，不重复，且顺序和students相对应
numbers=[]
with open('pythonsign_20181009.csv')as f1:
    reader1=csv.reader(f1)
    header_row1=next(reader1)
    #从第二行开始读取

    for row in reader1:
        """由于是第一个文件，所有学号都是第一次出现，直接添加即可"""
        arrived.append(row[0])
        numbers.append(row[0])
        student={'学号':row[0],'姓名':row[1],'班级':row[2]}
        students.append(student)
    
with open ('pythonsign_20181030.csv')as f2:
    reader2=csv.reader(f2)
    header_row2=next(reader2)
    #从第二行开始读取
    
    for row in reader2:
        #出现的学号都加入arrived列表中
        arrived.append(row[0])
        if row[0] not in numbers:
            #新签到的同学，把他加入students和numbers列表中
            student={'学号':row[0],'姓名':row[1],'班级':row[2]}
            students.append(student)
            numbers.append(row[0])
                
with open ('pythonsign_20181030.csv')as f3:
    reader3=csv.reader(f3)
    headder_row3=next(reader3)
    #c从第二行开始读取
    
    for row in reader3:
        #出现的学号都加入arrived列表中
        arrived.append(row[0])
        if row[0] not in arrived:
            #新签到的同学，把他加入students和numbers列表中
            student={'学号':row[0],'姓名':row[1],'班级':row[2]}
            students.append(student)
            numbers.append(row[0])

frequencies=[]
#数出每个学号共出现了几次，并存入frequencies中
for value in students:
    frequency=arrived.count(value['学号'])
    frequencies.append(frequency)

#创建一个csv文件，并写入需要的信息
with open("arrived results.csv","w",newline="") as r:
    writer=csv.writer(r)
    writer.writerow(['学号','姓名','班级','签到次数'])
    for i in range(len(students)):
        #按行写入数据
        writer.writerow([students[i]['学号'],students[i]['姓名'],
                          students[i]['班级'],frequencies[i]])

#绘制图表并显示
plt.scatter(numbers,frequencies,edgecolor='blue')
plt.show()
