import csv
from matplotlib import pyplot as plt
filename="pythonsign_20181009.csv"
with open (filename) as f:#打开文件
    reader=csv.reader(f)
    header_now=next(reader)
    print(header_now)
    IDs=[]
    names=[]
    Classes=[]
    counts=[]
    for row in reader:
        ID=row[0]
        name=row[1]
        Class=row[3]#依次读入ID，name，Class并保存在相应变量中
        if name not in names and ID not in IDs:#如果之前没有该学生就添加其信息
            IDs.append(ID)
            names.append(name)
            Classes.append(Class)
            counts.append(1)
        elif name in names and ID not in IDs:#之前有该学生信息，但是名称正确，学号错误
            num=names.index(name)
            counts[num]=counts[num]+1
        elif ID in IDs and name not in names:#之前有该学生信息，但是学号正确，名称错误
            num=IDs.index(ID)
            counts[num]=counts[num]+1
        elif ID in IDs and name in names:#之前有该学生信息
            num=IDs.index(ID)
            counts[num]=counts[num]+1

filename="pythonsign_20181030.csv"
with open (filename) as f:
    reader=csv.reader(f)
    header_now=next(reader)
    print(header_now)
    for row in reader:
        ID=row[0]
        name=row[1]
        Class=row[3]
        if name not in names and ID not in IDs:#如果之前没有该学生就添加其信息
            IDs.append(ID)
            names.append(name)
            Classes.append(Class)
            counts.append(1)
        elif name in names and ID not in IDs:#之前有该学生信息，但是名称正确，学号错误
            num=names.index(name)
            counts[num]=counts[num]+1
        elif ID in IDs and name not in names:#之前有该学生信息，但是学号正确，名称错误
            num=IDs.index(ID)
            counts[num]=counts[num]+1
        elif ID in IDs and name in names:#之前有该学生信息
            num=IDs.index(ID)
            counts[num]=counts[num]+1

filename="pythonsign_20181113.csv"
with open (filename) as f:
    reader=csv.reader(f)
    header_now=next(reader)
    print(header_now)
    for row in reader:
        ID=row[0]
        name=row[1]
        Class=row[3]
        if name not in names and ID not in IDs:#如果之前没有该学生就添加其信息
            IDs.append(ID)
            names.append(name)
            Classes.append(Class)
            counts.append(1)
        elif name in names and ID not in IDs:#之前有该学生信息，但是名称正确，学号错误
            num=names.index(name)
            counts[num]=counts[num]+1
        elif ID in IDs and name not in names:#之前有该学生信息，但是学号正确，名称错误
            num=IDs.index(ID)
            counts[num]=counts[num]+1
        elif ID in IDs and name in names:#之前有该学生信息
            num=IDs.index(ID)
            counts[num]=counts[num]+1
            
with open('result','w') as file_object:
    for i in range(1,len(IDs)):
        student=IDs[i-1]+" "+names[i-1]+" "+Classes[i-1]+" "+str(counts[i-1])+"\n"
        file_object.write(student)#写入信息
fig=plt.figure(dpi=128,figsize=(30,20))
plt.scatter(IDs,counts,c='blue')
fig.autofmt_xdate()
plt.tick_params(axis='both',labelsize=3)
plt.show()            
        
