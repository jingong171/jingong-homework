import csv
import matplotlib.pyplot as plt

file1="pythonsign_20181009.csv"
file2="pythonsign_20181030.csv"
file3="pythonsign_20181113.csv"
ids,names,classes,nums=[],[],[],[]
with open(file1) as f1:
    """对file1出现的人计数"""
    reader1=csv.reader(f1)
    headrow1=next(reader1)
    for row in reader1:
        try:
            id=int(row[0])
            name=str(row[1])
            classs=str(row[3])
        except ValueError:
            pass
        else:
            ids.append(id)
            names.append(name)
            classes.append(classs)
            nums.append(1)

with open(file2) as f2:
    """继续计数，file1中出现的人count只要加1，file1没出现的从1开始计数"""
    reader2=csv.reader(f2)
    headrow2=next(reader2)
    for row in reader2:
        try:
            id=int(row[0])
            name=str(row[1])
            classs=str(row[3])
        except ValueError:
            pass
        else:
            if id in ids:
                nums[ids.index(id)]+=1
            else:
                ids.append(id)
                names.append(name)
                classes.append(clas)
                nums.append(1)

with open(file3) as f3:
    """继续计数"""
    reader3=csv.reader(f3)
    headrow3=next(reader3)
    for row in reader3:
        try:
            id=int(row[0])
            name=str(row[1])
            clas=str(row[3])
        except ValueError:
            pass
        else:
            if id in ids:
                nums[ids.index(id)]+=1
            else:
                ids.append(id)
                names.append(name)
                classes.append(clas)
                nums.append(1)

with open("results.txt",'w') as fo:
    """把计数结果写入文件"""
    fo.write("%s %15s %6s %4s"%("学号","姓名","签到次数","班级")+"\n")
    for i in range(len(ids)):
        fo.write("%10d %3s %6d %10s"%(ids[i],names[i],counts[i],classes[i])+"\n")

"""作图"""
list=list(range(1,len(ids)+1))
fig=plt.figure(dpi=128,figsize=(10,6))
plt.scatter(list,nums,edgecolor='none',c='blue',s=20)
plt.title("Total Counts of All Students",fontsize=24)
plt.xlabel("Students No.",fontsize=16)
plt.ylabel("Nums",fontsize=16)
plt.tick_params(axis="both",which="major",labelsize=16)
fig.tight_layout()
plt.show()