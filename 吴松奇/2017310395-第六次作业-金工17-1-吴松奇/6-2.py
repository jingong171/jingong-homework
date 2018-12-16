import csv
import matplotlib.pyplot as plt
filename1="pythonsign_20181009.csv"
filename2="pythonsign_20181030.csv"
filename3="pythonsign_20181113.csv"
with open(filename1) as f:
    reader=csv.reader(f)
    header_row=next(reader)
    numbers=[]
    names=[]
    classes=[]
    times=[]
    for row in reader:
        name=row[1]
        names.append(name)
        number=row[0]
        numbers.append(number)
        class_=row[3]
        classes.append(class_)
        time=row[7]
        times.append(time)
with open(filename2) as f2:
    reader2=csv.reader(f2)
    header_row2=next(reader2)
    numbers2=[]
    names2=[]
    classes2=[]
    times2=[]
    for row in reader2:
        name2=row[1]
        names2.append(name2)
        number2=row[0]
        numbers2.append(number2)
        class_2=row[3]
        classes2.append(class_2)
        time2=row[7]
        times2.append(time2)
with open(filename3) as f3:
    reader3=csv.reader(f3)
    header_row3=next(reader3)
    numbers3=[]
    names3=[]
    classes3=[]
    times3=[]
    for row in reader3:
        name3=row[1]
        names3.append(name3)
        number3=row[0]
        numbers3.append(number3)
        class_3=row[3]
        classes3.append(class_3)
        time3=row[7]
        times3.append(time3)
for i in range(len(names)):
    if names2[i] not in names:
        names.append(names2[i])
        numbers.append(numbers2[i])
        classes.append(classes2[i])
        times.append(times2[i])
for i in range(len(names)):
    if names3[i] not in names:
        names.append(names3[i])
        numbers.append(numbers3[i])
        classes.append(classes3[i])
        times.append(times3[i])
frequencies=[]
names_=names+names2+names3
for name in names:
    frequency=names_.count(name)
    frequencies.append(frequency)

plt.scatter(names,frequencies,edgecolor='blue')
plt.show()
out=open("签到次数.csv","a",newline="")
csv_write=csv.writer(out,dialect="excel")
for i in range(len(names)):
    csv_write.writerow([numbers[i],names[i],classes[i],times[i]])
out.close()
print("write over")
