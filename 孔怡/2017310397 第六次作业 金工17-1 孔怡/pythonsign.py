import csv
import pygal
import matpoltlib.python as plt

numbers,students,classes,num_arrived=[],[],[],[]
with open("pythonsign_20181009.csv")as f1:
    reader1=csv.reader(f1)
    header_row1=next(reader1)

    for row in reader1:
       try:
            number.int(row[0])
            student.str(row[1])
            class_.str(row[3])
        except ValueError:
            pass
        else:
            numbers.append(number)
            students.append(students)
            classes.append(class_)
            num_arrived.append(1)

with open("pythonsign_20181030.csv")as f2:
    reader2=csv.reader(f2)
    header_row2=next(reader2)

    for row in reader2:
        try:
            number.int(row[0])
            student.str(row[1])
            class_.str(row[3])
        except ValueError:
            pass
        else:
            numbers.append(number)
            students.append(students)
            classes.append(class_)
            num_arrived.append(1)
            
with open("pythonsign_20181113.csv")as f3:
    reader3=csv.reader(f3)
    header_row3=next(reader3)

    for row in reader3:
        try:
            number.int(row[0])
            student.str(row[1])
            class_.str(row[3])
        except ValueError:
            pass
        else:
            numbers.append(number)
            students.append(students)
            classes.append(class_)
            num_arrived.append(1)

student_in[]
for st in student:
    if st not in student_in:
        student_in.append(st)
    else:
        continue
    
frequencies=[]
for student in students:
    frequency=num_arrived.count(student)
    frequencies.append(frequency)

with open("arrived results.csv","w",)as ar:
    ar.write("%s %15s %6s %4s"%("学号","姓名","签到次数","班级")+"\n")    
    for i in range(len(numbers)):
        ar.write("%10d %3s %6d %10s"%(numbers[i],names[i],num_arrived[i],classes[i])+"\n")

list=list(range(1,len(numbers)+1))

fig=plt.figure(dpi=128,figsize=(10,6))
plt.scatter(list,num_arrived,edgecolor='none',c='blue',s=20)
plt.title("Total Counts of All Students",fontsize=24)
plt.xlabel("Students No.",fontsize=16)
plt.ylabel("Num_arrived",fontsize=16)
plt.tick_params(axis="both",which="major",labelsize=16)
fig.tight_layout()
plt.show()
        
