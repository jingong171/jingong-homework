import csv
import matplotlib.pyplot as plt


filename_1='pythonsign_20181009.csv'
filename_2='pythonsign_20181030.csv'
filename_3='pythonsign_20181113.csv'
peoples=[]

#open three files and save the datas into peoples
with open(filename_1)as f:
    reader_1=csv.reader(f)
    
    for row in reader_1:
        people={}
        st_number=row[0]
        na=row[1]
        cl=row[3]
        people['ID']=st_number
        people['name']=na
        people['class']=cl
        
        peoples.append(people)
with open(filename_2)as f:
    reader_2=csv.reader(f)
    
    for row in reader_2:
        people={}
        st_number=row[0]
        na=row[1]
        cl=row[3]
        people['ID']=st_number
        people['name']=na
        people['class']=cl
        peoples.append(people)
with open(filename_3)as f:
    reader_3=csv.reader(f)
    
    for row in reader_3:
        people={}
        st_number=row[0]
        na=row[1]
        cl=row[3]
        people['ID']=st_number
        people['name']=na
        people['class']=cl
        peoples.append(people)

myset=[]
names=[]
name1=[]
count=[]
names2=[]

#get all names
for i in peoples:
    name=i['name']
    name1.append(name)

#delete repetitive names
for i in peoples:
    
    ne=i['name']
    if not ne in names:
        myset.append(i)
        names.append(ne)

#get times
for item2 in myset:
    c = name1.count(item2['name'])
    item2['count'] = c
print (myset)

#paint
fig=plt.figure(dpi=128,figsize=(10,6)
for i in myset:
    na=i['name']
    co=i['count']
    names2.append(name)
    count.append(co)
plt.scatter(names2,count, c='blue')
plt.title("the frequencies of sutdents' signature", fontsize=24)
plt.xlabel("name", fontsize=12)
plt.ylabel("frequencies", fontsize=12)
plt.show()




