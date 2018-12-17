import csv
from matplotlib import pyplot as plt


filename_1="pythonsign_20181009.csv"
filename_2="pythonsign_20181030.csv"
filename_3="pythonsign_20181113.csv"
with open(filename_1,) as f1:
    reader=csv.reader(f1)
    header_row= next(reader)

    for row in reader:
        try:
            idnums=[]
            names=[]
            clases=[]
            idnum=int(row[0])
            name=str(row[1])
            clas=str(row[3])
            
        except ValueError:
            pass
        else:
            clases=append(clas)
            names=append(name)
            idnums=append(idnum)
            num_arrived.append(1)



with open(filename_2) as f2:
    reader=csv.reader(f2)
    header_row=next(reader)

    for row in reader:
        try:
            idnums=[]
            names=[]
            clases=[]
            idnum=int(row[0])
            name=str(row[1])
            clas=str(row[3])
        except ValueError:
            pass
        else:
            clases=append(clas)
            names=append(name)
            idnums=append(idnum)
            num_arrived.append(1)


with open(filename_3) as f3:
    reader=csv.reader(f3)
    header_row=next(reader)

    for row in reader:
        try:
            idnums=[]
            names=[]
            clases=[]
            idnum=int(row[0])
            name=str(row[1])
            clas=str(row[3])
        except ValueError:
            pass
        else:
            clases=append(clas)
            names=append(name)
            idnums=append(idnum)
            num_arrived.append(1)


out=open("签到结果.csv","a",newline="")
csv_write=csv.writer(out,dialect="excel")
for i in range(len(names)):
    csv_write.writerow([idnums[i],names[i],clases[i],num_arrived[i]])
out.close()

frequencies=[]
for name in names:
    frequency=names.count(name)
    frequencies.append(frequency)


x_values=range(1,len(names)+1)
y_values=frequencies
plt.title("签到结果分布图",fontsize=28)
plt.scatter(x_values,y_values,c='blue',edgecolors='none',s=15)
plt.xlabel("学生姓名",fontsize=24)
plt.ylabel("签到次数",fontsize=24)
plt.show()



                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              