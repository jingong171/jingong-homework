import matplotlib.pyplot as plt
import csv
zi={}
list1,list2,list3=[],[],[]
filename1 ='pythonsign_20181009'
with open(filename1) as f1:
    reader1 = csv.reader(f1)
    header_row = next(reader1)
    for row in reader1:
        xuehao= int(row[0])   
        list1.append(xuehao)
    for row in reader1:
        a[row[0]]=row[1: ]
        

filename2 ='pythonsign_20181030'
with open(filename2) as f2:
    reader2 = csv.reader(f2)
    header_row = next(reader2)
    for row in reader2:
        xuehao= int(row[0])   
        list2.append(xuehao)
    for row in reader2:
        a[row[0]]=row[1: ]


filename3 ='pythonsign_20181113'
with open(filename3) as f3:
    reader3 = csv.reader(f1)
    header_row = next(reader3)
    for row in reader3:
        xuehao= int(row[0])   
        list3.append(xuehao)
    for row in reader3:
        a[row[0]]=row[1: ]


# 计算签到次数

#思路：把三个列表都合并到列表klist中，然后用set去除相同的项得到llist
#然后做一个字典，键为llist，值为0
#遍历列表klist，遇到一个学号，然后把字典中的值加1
#最后字典中的值就是学号对应的签到次数
klist=[]
for a in list1:
    klist.append(a)
for b in list2:
    klist.append(b)
for c in list3:
    klist.append(c)
llist = list(set(klist))
b={}
for i in llist:
    b[i]=0
for i in klist:
    b[i]+=1
            
#制作表格
#抱歉老师，这个问题用现有知识做不出来

#制散点图
plt.figure(dpi=128, figsize=(10,6))
plt.scatter( llist,b.value(),c='blue' ,edgecolor='none', s=15)
plt.title("签到统计", fontsize=24)
plt.xlabel("学号", fontsize = 14)
plt.ylabel("次数", fontsize = 14)
plt.tick_params(axis = 'both', which = 'major', labelsize = 14)

plt.show()
            
