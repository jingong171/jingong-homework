# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 14:13:15 2018

@author: WSQ
"""

import csv
import matplotlib.pyplot as plt

filename_1="pythonsign_20181009.csv"
filename_2="pythonsign_20181030.csv"
filename_3="pythonsign_20181113.csv"
arrival,students,counts=[],[],[]
with open(filename_1) as f1:
    reader_1=csv.reader(f1)
    head_row_1=next(reader_1)
    for row in reader_1:
        try:
            arrival.append(row[0])
            counts.append(row[0])
            student={'学号':row[0],'姓名':row[1],'班级':row[2]}
            students.append(student)
        except ValueError:
            pass

with open(filename_2) as f2:
    reader2=csv.reader(f2)
    head_row_2=next(reader2)
    for row in reader2:
        try:
            arrival.append(row[0])
        except ValueError:
            pass
        else:
            if row[0] in counts:
                student={'学号':row[0],'姓名':row[1],'班级':row[2]}
                students.append(student)
                counts.append(row[0])
            else:
                pass
    
with open(filename_3) as f3:
    reader_3=csv.reader(f3)
    head_row3=next(reader_3)
    for row in reader_3:
        try:
            arrival.append(row[0])
        except ValueError:
            pass
        else:
            if row[0] not in arrival:
            #新签到的同学，把他加入students和numbers列表中
                student={'学号':row[0],'姓名':row[1],'班级':row[2]}
                students.append(student)
                counts.append(row[0])
            else:
                pass
            
numbers=[]
for value in students:
    number=arrival.count(value['学号'])
    numbers.append(number)

with open("arrived results.csv","w",newline="") as r:
    csv=csv.writer(r)
    csv.writerow(['学号','姓名','班级','签到次数'])
    for i in range(len(students)):
        csv.writerow([students[i]['学号'],students[i]['姓名'],students[i]['班级'],numbers[i]])
        plt.scatter(students[i]['姓名'],number,c='blue',s=10)
        plt.title("签到统计",fontsize=24)
        plt.xlabel("学生名字",fontsize=14)
        plt.ylabel("次数",fontsize=14)
        plt.tick_params(axis='x',labelsize=4)
        plt.show()