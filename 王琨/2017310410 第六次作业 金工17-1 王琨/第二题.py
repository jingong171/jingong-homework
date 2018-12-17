import csv
import matplotlib.pyplot as plt

filename1='pythonsign_20181009.csv'
filename2='pythonsign_20181030.csv'
filename3='pythonsign_20181113.csv'

with open(filename1) as f1:
    reader1=csv.reader(f1)
    header_row1=next(reader1)
    reg_num1,name1,class1=[],[],[]
    for row in reader1:
        try:
            reg_num=int(row[0])
            name=str(row[1])
            clas=str(row[3])
        except ValueError:
            pass
        else:
            reg_num1.append(reg_num)
            name1.append(name)
            class1.append(clas)
           
with open(filename2) as f2:
    reader2=csv.reader(f2)
    header_row2=next(reader2)
    reg_num2,name2,class2=[],[],[]
    for row in reader2:
        try:
            reg_num=int(row[0])
            name=str(row[1])
            clas=str(row[3])
        except ValueError:
            pass
        else:
            reg_num2.append(reg_num)
            name2.append(name)
            class2.append(clas)

with open(filename3) as f3:
    reader3=csv.reader(f3)
    header_row3=next(reader3)
    reg_num3,name3,class3=[],[],[]
    for row in reader3:
        try:
            reg_num=int(row[0])
            name=str(row[1])
            clas=str(row[3])
        except ValueError:
            pass
        else:
            reg_num3.append(reg_num)
            name3.append(name)
            classe3.append(clas)
 
for i in range(len(name1)):
    if name2[i] not in name1:
        reg_num1.append(reg_num2[i])
        name1.append(name2[i])
        class1.append(class2[i])

for i in range(len(name1)):
    if name3[i] not in name1:
        reg_num1.append(reg_num3[i])
        name1.append(name3[i])
        class1.append(class3[i])

frequencies=[]
names=name1+name2+name3
for name in names:
    frequency=names.count(name)
    frequencies.append(frequency)

plt.scatter(names,frequencies,s=100)
plt.show()
out=open("签到次数.csv","a",newline="")
csv_write=csv.writer(out,dialect="excel")
for i in range(len(names)):
     csv_write.writerow([reg_num1[i],name1[i],class1[i]])
out.close()
            
