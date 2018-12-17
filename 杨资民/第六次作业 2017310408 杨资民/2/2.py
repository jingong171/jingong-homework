import csv
import matplotlib.pyplot as plt

filename_1="pythonsign_20181009.csv"
filename_2="pythonsign_20181030.csv"
filename_3="pythonsign_20181113.csv"
ID_many=[]
Name_many=[]
Class_many=[]
Count_many=[]

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
            ID_many.append(ID)
            Name_many.append(Name)
            Class_many.append(Class)
            Count_many.append(1)

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
            if ID in ID_many:
                Count_many[ID_many.index(ID)]+=1
            else:#对于没有出现在文件1里面的计数
                ID_many.append(ID)
                Name_many.append(Name)
                Class_many.append(Class)
                Count_many.append(1)
    
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
            if ID in ID_many:
                Count_many[ID_many.index(ID)]+=1
            else:#对于没有出现在文件1、2里面的计数
                ID_many.append(ID)
                Name_many.append(Name)
                Class_many.append(Class)
                Count_many.append(1)

filename="restults.txt"#输出
with open(filename,'w') as f:
    f.write("%s %15s %6s %4s"%("学号","姓名","签到次数","班级")+"\n")    
    for i in range(len(ID_many)):
        f.write("%10d %3s %6d %10s"%(ID_many[i],Name_many[i],Count_many[i],Class_many[i])+"\n")

list=list(range(1,len(ID_many)+1))

fig=plt.figure(dpi=128,figsize=(10,6))#绘图
plt.scatter(list,Count_many,edgecolor='none',c='blue',s=25)
plt.title("Count_many",fontsize=25)
plt.xlabel("Students No.",fontsize=18)
plt.ylabel("Count_many",fontsize=18)
plt.tick_params(axis="both",which="major",labelsize=18)
fig.tight_layout()
plt.show()
