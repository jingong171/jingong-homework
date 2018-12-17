import csv
import matplotlib.pyplot as plt
#将包导入

filename1="pythonsign_20181009.csv"
filename2="pythonsign_20181030.csv"
filename3="pythonsign_20181113.csv"

ids,names,classes,counts=[],[],[],[]
#建立四个空列表

with open(filename1) as f1:
    reader1=csv.reader(f1)
    head_row1=next(reader1)
    for row in reader1:
        try:
            id=int(row[0])
            name=str(row[1])
            clas=str(row[3])
        except ValueError:
            pass
        else:
            ids.append(id)
            names.append(name)
            classes.append(clas)
            counts.append(1)

 with open(filename2) as f2:
    reader2=csv.reader(f2)
    head_row2=next(reader2)
    for row in reader2:
        try:
            id=int(row[0])
            name=str(row[1])
            clas=str(row[3])
        except ValueError:
            pass
        else:
            if id in ids:
                counts[ids.index(id)]+=1
            else:
                ids.append(id)
                names.append(name)
                classes.append(clas)
                counts.append(1)
    
with open(filename3) as f3:
    reader3=csv.reader(f3)
    head_row3=next(reader3)
    for row in reader3:
        try:
            id=int(row[0])
            name=str(row[1])
            clas=str(row[3])
        except ValueError:
            pass
        else:
            if id in ids:
                counts[ids.index(id)]+=1
            else:
                ids.append(id)
                names.append(name)
                classes.append(clas)
                counts.append(1)

#将三次点名文件统计
                
filename="total_counts.txt"

with open(filename,'w') as f:
    f.write("%s %15s %6s %4s"%("学号","姓名","签到次数","班级")+"\n")    
    for i in range(len(ids)):
        f.write("%10d %3s %6d %10s"%(ids[i],names[i],counts[i],classes[i])+"\n")
list=list(range(1,len(ids)+1))
#按照"total_counts.txt"中学生顺序进行编号

fig=plt.figure(dpi=128,figsize=(10,6))
plt.scatter(list,counts,edgecolor='none',c='blue',s=20)
plt.title("Total Counts of All Students",fontsize=24)
plt.xlabel("Students No.",fontsize=16)
plt.ylabel("Counts",fontsize=16)
plt.tick_params(axis="both",which="major",labelsize=16)
fig.tight_layout()
#可视化
plt.show()
