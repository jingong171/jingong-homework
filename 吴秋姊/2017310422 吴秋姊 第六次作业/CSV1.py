import csv

# Get IDs, names, and classes from file.
filename = 'pythonsign_20181009.csv'
with open(filename) as f1:
    reader = csv.reader(f1)
    header_row = next(reader)
    IDs=[]
    names = []
    Classes=[]
    for row in reader:
        ID=(row[0])
        name = (row[1])
        Class=(row[3])
        IDs.append(ID)
        names.append(name)
        Classes.append(Class)
        
    
filename = 'pythonsign_20181030.csv'
with open(filename) as f2:
    reader = csv.reader(f2)
    header_row = next(reader)        
    for row in reader:
        ID=(row[0])
        name = (row[1])
        Class=(row[3])
        IDs.append(ID)
        names.append(name)
        Classes.append(Class)

    
filename = 'pythonsign_20181113.csv'
with open(filename) as f1:
    reader = csv.reader(f1)
    header_row = next(reader)
    for row in reader:
        ID=(row[0])
        name = (row[1])
        Class=(row[3])
        IDs.append(ID)
        names.append(name)
        Classes.append(Class)

#用count记数
frequencies=[]

for name in names:
    if names.count(name):
        frequency=names.count(name)
        frequencies.append(frequency)


##将列表合并成一个字典
dic1={}
for ID,name,Class,frequency in zip(IDs,names,Classes,frequencies): 
    #print(ID,name,Class,frequency)
    dic1[name] = ID,Class,frequency
##print(dic1)

import json
#存储成为json格式文件

json_str=json.dumps(dic1,ensure_ascii=False)
with open('pythonsign.json', 'w') as json_file:
    json_file.write(json_str)

import matplotlib.pyplot as plt

x_values = names
y_values = frequencies
plt.scatter(x_values,y_values, s = 20)

plt.title("sign_counter", fontsize=24)
plt.xlabel("Value", fontsize = 14)
plt.ylabel("count", fontsize = 14)

plt.tick_params(axis = 'both', which = 'major', labelsize = 14)
plt.show()

