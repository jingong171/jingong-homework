import csv
from matplotlib import pyplot as plt
filename1 ="pythonsign_20181009.csv"
filename2 ="pythonsign_20181030.csv"
filename3 ="pythonsign_20181113.csv"
filenames=[filename1,filename2,filename3]
ids,names,classes,times =[],[],[],[]
with open(filename1) as f1:
    reader1=csv.reader(f1)
    head_row1=next(reader1)
    for row in reader1:
        try:
            stu_id=int(row[0])
            name=str(row[1])
            classe=str(row[3])
        except ValueError:
            pass
        else:
            ids.append(stu_id)
            names.append(name)
            classes.append(classe)
            times.append(1)
with open(filename2) as f2:
    reader2=csv.reader(f2)
    head_row2=next(reader2)
    for row in reader2:
        try:
            stu_id=int(row[0])
            name=str(row[1])
            classe=str(row[3])
        except ValueError:
            pass
        else:
            if stu_id in ids:
                times[ids.index(stu_id)]+=1
            else:
                ids.append(stu_id)
                names.append(name)
                classes.append(classe)
                times.append(1)
    
with open(filename3) as f3:
    reader3=csv.reader(f3)
    head_row3=next(reader3)
    for row in reader3:
        try:
            stu_id=int(row[0])
            name=str(row[1])
            classe=str(row[3])
        except ValueError:
            pass
        else:
            if stu_id in ids:
                times[ids.index(stu_id)]+=1
            else:
                ids.append(stu_id)
                names.append(name)
                classes.append(classe)
                times.append(1)
filename_final="total_sign_in_times.csv"
with open(filename_final,'w',newline="") as f:
    writer=csv.writer(f)
    writer.writerow(["学号","姓名","签到次数","班级"])    
    for i in range(len(ids)):
        writer.writerow([ids[i],names[i],times[i],classes[i]])
x_values=list(range(1,len(ids)+1))
y_values=times
plt.scatter(x_values,y_values,c='blue',edgecolor='none',s=40)
plt.title("Total of All Students Sign In Times",fontsize=24)
plt.xlabel("Students ID",fontsize=16)
plt.ylabel("Times",fontsize=16)
plt.tick_params(axis="both",which="major",labelsize=16)
plt.show()
