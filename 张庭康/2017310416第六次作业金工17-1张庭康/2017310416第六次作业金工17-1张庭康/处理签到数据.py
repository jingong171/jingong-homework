import csv

#声明文件名
filename_1='pythonsign_20181009.csv'
filename_2='pythonsign_20181030.csv'
filename_3='pythonsign_20181113.csv'

#建立数组用于存放数据
peoples=[]

#分别打开三个文件，把有关数据存在peoples中

with open(filename_1) as f:
    reader_1=csv.reader(f)
    
    for row in reader_1:
        people = {}
        st_number = row[0]
        name = row[1]
        Class = row[3]
        people['ID'] = st_number
        people['name'] = name
        people['class'] = Class
        peoples.append(people)
        
with open(filename_2)as f:
    reader_2=csv.reader(f)
    
    for row in reader_2:
        people={}
        st_number=row[0]
        name=row[1]
        Class=row[3]
        people['ID']=st_number
        people['name']=name
        people['class']=Class
        peoples.append(people)
        
with open(filename_3)as f:
    reader_3=csv.reader(f)
    
    for row in reader_3:
        people={}
        st_number=row[0]
        name=row[1]
        Class=row[3]
        people['ID']=st_number
        people['name']=name
        people['class']=Class
        peoples.append(people)
        
#对重复的数据进行筛选，并将重复次数作为签到次数
myset = []
names = []
name1 = []
count = []
names2 = []

#先将所有的名字提取出来
for i in peoples:
    na=i['name']
    name1.append(na)
    
#根据名字是否重复进行数据重复剔除
for i in peoples:
    ne=i['name']
    if not ne in names:
        myset.append(i)
        names.append(ne)
        
#再根据全部提出的名字进行计数签到次数
for item2 in myset:
    c = name1.count(item2['name'])
    item2['count'] = c
print (myset)

#开始制作图表
from matplotlib import pyplot as plt

for i in myset:
    na=i['name']
    co=i['count']
    names2.append(na)
    count.append(co)
plt.scatter(names2,count, c='blue')
"确定横纵坐标的值"
plt.title("Dispersed map of student checkins", fontsize=20)
"输入标题"
plt.xlabel("name", fontsize=12)
"横坐标的标题和字号"
plt.ylabel("Number of check-ins", fontsize=12)

plt.show()
"输出图表"








