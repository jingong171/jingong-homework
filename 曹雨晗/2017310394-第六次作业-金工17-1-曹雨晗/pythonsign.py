import csv
from matplotlib import pyplot as plt

#从第一个文件中提取信息
filename = 'pythonsign_20181009.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    #定义一个空列表存储所有的学生
    student_id = []
    #定义一个空列表存储第一次签到到来的学生
    student_id1 = []
    #定义一个空列表存储到来的次数
    times = []
    for row in reader:
        number = row[0]
        arrive = 1
        student_id.append(number)
        student_id1.append(number)
        times.append(arrive)

#从第二个文件中提取信息
filename = 'pythonsign_20181030.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    #定义一个空列表存储第二次签到来的学生
    student_id2 = []
    #定义一个计数变量i，来计数学生的个数
    i = 0
    for row in reader:
        number = row[0]
        student_id2.append(number)
        if row[0] in student_id1:
        #第一次和第二次签到都来
            times[i] = 2
        else:
        #第一次没来但是第二次来了
            student_id.append(number)
            arrive = 1
            times.append(arrive)
        i = i+1

#从第三个文件中提取信息,过程与第二个文件提取信息过程相似
filename = 'pythonsign_20181113.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    i = 0
    for row in reader:
        if row[0] in student_id1:
            if row[0] in student_id2:
            #三次都来了
                times[i] = 3
            else:
            #第一次和第三次来了
                times[i] = 2
        else:
            if row[0] in student_id2:
            #第二次和第三次来了
                times[i] = 2
            else:
            #只有第三次来了
                number = row[0]
                student_id.append(number)
                arrive = 1
                times.append(arrive)
        i = i+1


#开始可视化的步骤
x_values = student_id
y_values = times
plt.scatter(x_values, y_values, edgecolor = 'none', c = 'blue', s = 40)
plt.title("Python Sign Times of All of the Students", fontsize = 24)
plt.xlabel("Students'ID", fontsize = 14)
plt.ylabel("Times", fontsize = 14)
plt.show()
