import csv
from matplotlib import pyplot as plt
ids,names,classes=[],[],[]
def file_read(filename):
    with open(filename) as f:
        reader=csv.reader(f)
        header_row=next(reader)
        for row in reader:
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
filenames=['pythonsign_20181009.csv','pythonsign_20181030.csv','pythonsign_20181113.csv']
for filename in filenames:
    file_read(filename)
times=[]
for name in names:
    time=names.count(name)
    times.append(time)
filename_final="total_sign_in_times.csv"
with open(filename_final,'w',newline="") as f:
    writer=csv.writer(f)
    writer.writerow(["学号","姓名","签到次数","班级"])    
    for i in range(len(ids)):
        writer.writerow([ids[i],names[i],times[i],classes[i]])
plt.scatter(names,times,c='blue')
plt.title("Total of All Students Sign In Times")
plt.xlabel("Name")
plt.ylabel("Times")
plt.show()



