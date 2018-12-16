import csv
import matplotlib.pyplot as plt

filename_1="pythonsign_20181009.csv"
filename_2="pythonsign_20181030.csv"
filename_3="pythonsign_20181113.csv"
IDs=[]
Names=[]
Classes=[]
Counts=[]

with open(filename_1) as f_1:#对于文件1计数
    reader_1=csv.reader(f_1)
    head_row_1=next(reader_1)
    for row in reader_1:
        try:
            ID=int(row[0])
            Name=str(row[1])
            Class=str(row[3])
        except ValueError:
            pass
        else:
            IDs.append(ID)
            Names.append(Name)
            Classes.append(Class)
            Counts.append(1)

with open(filename_2) as f_2:#对于文件2计数
    reader_2=csv.reader(f_2)
    head_row_2=next(reader_2)
    for row in reader_2:
        try:
            ID=int(row[0])
            Name=str(row[1])
            Class=str(row[3])
        except ValueError:
            pass
        else:
            if ID in IDs:
                Counts[IDs.index(ID)]+=1
            else:#对于没有出现在文件1里面的计数
                IDs.append(ID)
                Names.append(Name)
                Classes.append(Class)
                Counts.append(1)
    
with open(filename_3) as f_3:#文件3计数
    reader_3=csv.reader(f_3)
    head_row_3=next(reader_3)
    for row in reader_3:
        try:
            ID=int(row[0])
            Name=str(row[1])
            Class=str(row[3])
        except ValueError:
            pass
        else:
            if ID in IDs:
                Counts[IDs.index(ID)]+=1
            else:#对于没有出现在文件1、2里面的计数
                IDs.append(ID)
                Names.append(Name)
                Classes.append(Class)
                Counts.append(1)

filename="restults.txt"#输出
with open(filename,'w') as f:
    f.write("%s %15s %6s %4s"%("学号","姓名","签到次数","班级")+"\n")    
    for i in range(len(IDs)):
        f.write("%10d %3s %6d %10s"%(IDs[i],Names[i],Counts[i],Classes[i])+"\n")

list=list(range(1,len(IDs)+1))

fig=plt.figure(dpi=128,figsize=(10,6))#绘图
plt.scatter(list,Counts,edgecolor='none',c='blue',s=25)
plt.title("Counts",fontsize=25)
plt.xlabel("Students No.",fontsize=18)
plt.ylabel("Counts",fontsize=18)
plt.tick_params(axis="both",which="major",labelsize=18)
fig.tight_layout()
plt.show()
