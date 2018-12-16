import csv
from matplotlib import pyplot as plt
filename="pythonsign_20181009.csv"
with open (filename) as f:
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
        Class=row[3]
        if name not in names and ID not in IDs:
            IDs.append(ID)
            names.append(name)
            Classes.append(Class)
            counts.append(1)
        elif name in names and ID not in IDs:
            num=names.index(name)
            counts[num]=counts[num]+1
        elif ID in IDs and name not in names:
            num=IDs.index(ID)
            counts[num]=counts[num]+1
        elif ID in IDs and name in names:
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
        if name not in names and ID not in IDs:
            IDs.append(ID)
            names.append(name)
            Classes.append(Class)
            counts.append(1)
        elif name in names and ID not in IDs:
            num=names.index(name)
            counts[num]=counts[num]+1
        elif ID in IDs and name not in names:
            num=IDs.index(ID)
            counts[num]=counts[num]+1
        elif ID in IDs and name in names:
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
        if name not in names and ID not in IDs:
            IDs.append(ID)
            names.append(name)
            Classes.append(Class)
            counts.append(1)
        elif name in names and ID not in IDs:
            num=names.index(name)
            counts[num]=counts[num]+1
        elif ID in IDs and name not in names:
            num=IDs.index(ID)
            counts[num]=counts[num]+1
        elif ID in IDs and name in names:
            num=IDs.index(ID)
            counts[num]=counts[num]+1
            
with open('result','w') as file_object:
    for i in range(1,len(IDs)):
        student=IDs[i-1]+" "+names[i-1]+" "+Classes[i-1]+" "+str(counts[i-1])+"\n"
        file_object.write(student)
fig=plt.figure(dpi=128,figsize=(30,20))
plt.scatter(IDs,counts,c='blue')
fig.autofmt_xdate()
plt.tick_params(axis='both',labelsize=3)
plt.show()            
        
