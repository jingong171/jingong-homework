import matplotlib.pyplot as plt
import csv
file1='C:/Users/孙林轩/Desktop/pythonsign_20181009.csv'
file2='C:/Users/孙林轩/Desktop/pythonsign_20181030.csv'
file3='C:/Users/孙林轩/Desktop/pythonsign_20181113.csv'
with open(file1) as f1:
    reader1=csv.reader(f1)
    headline=next(reader1)
    lis_sign1=[]
    sign1=[]
    for row in reader1:
        lis_sign1.append(row[1])
        sign1.append([row[0],row[2],row[3],row[4]])

with open(file2) as f2:
    reader2=csv.reader(f2)
    headline=next(reader2)
    lis_sign2=[]
    sign2 = []
    for row in reader2:
        lis_sign2.append(row[1])
        sign2.append([row[0],row[2],row[3],row[4]])

with open(file3) as f3:
    reader3=csv.reader(f3)
    headline=next(reader3)
    lis_sign3=[]
    sign3=[]
    for row in reader3:
        lis_sign3.append(row[1])
        sign3.append([row[0],row[2],row[3],row[4]])

lis=[]
lis1=[]
if len(lis_sign1)>max(len(lis_sign2),len(lis_sign3)):
    lis=lis_sign1
    lis1=sign1
if len(lis_sign2)>max(len(lis_sign1),len(lis_sign3)):
    lis=lis_sign2
    lis1 = sign2
else:
    lis=lis_sign3
    lis1 = sign3
sign_num={}
i=0
for a in lis:
    if ((a in lis_sign1) and (a in lis_sign2) and (a in lis_sign3)):
        lis1[i].append('3')
        sign_num[a]=lis1[i]
        i+=1
    elif (((a in lis_sign1) and (a in lis_sign2)) or ((a in lis_sign3) and (a in lis_sign2)) or (a in lis_sign1) and (a in lis_sign3)):
        lis1[i].append('2')
        sign_num[a] = lis1[i]
        i += 1
    else:
        lis1[i].append('1')
        sign_num[a] = lis1[i]
        i += 1

f= open('C:/Users/孙林轩/Desktop/pythonSignAll.csv','w',newline='')
ik=0
c1=open(file1)
reader = csv.reader(c1)
header_row = next(reader)
writer = csv.writer(f)
header_row0=[header_row[1],header_row[0],header_row[2],header_row[3],header_row[4],'签到次数']
writer.writerow(header_row0)
for a in sign_num.keys():
    li=[a,lis1[ik][0],lis1[ik][1],lis1[ik][2],lis1[ik][3],lis1[ik][4]]
    writer.writerow(li)
    ik+=1
c1.close()
f.close()
signTimes=[]
for i in lis1:
    signTimes.append(i[4])
x_values=[range(1,len(lis)+1)]
y_values=[signTimes]
plt.figure(num=3, figsize=(13, 5))
plt.scatter(x_values, y_values, edgecolor='none',c='blue',s=10)
plt.show()