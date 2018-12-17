import csv
import pandas as pd
import matplotlib.pyplot as plt

filename = 'pythonsign_20181009.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    names = []
    numbers = []
    classes = []
    for row in reader:
        names.append(row[1])
        numbers.append(row[0])
        classes.append(row[3])
filename = 'pythonsign_20181030.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    for row in reader:
        names.append(row[1])
        numbers.append(row[0])
        classes.append(row[3])
filename = 'pythonsign_20181113.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    for row in reader:
        names.append(row[1])
        numbers.append(row[0])
        classes.append(row[3])
a = {}
for i in names:
    if names.count(i) >= 1:
         a[i] = names.count(i)
numbers_new = []
for i in numbers:
    if not i in numbers_new:
        numbers_new.append(i)
print(numbers_new)
names_new = []
signed_times = []
for k, v in a.items():
    names_new.append(k)
    signed_times.append(v)
list = [numbers_new, names_new, signed_times]
name = ['学号', '姓名', '出勤次数']
colummns=[]
for i in range(1, 106):
    i = ""
    colummns.append(i)
test = pd.DataFrame(index=name, columns=colummns, data=list)
print(test)
test.to_csv('E:/pycharm/1/round1/testcsv.csv', encoding='gbk')

x_values = numbers_new
y_values = signed_times
plt.title("python", fontsize=40)
plt.xlabel("number", fontsize=10)
plt.ylabel("signed_times", fontsize=10)
plt.scatter(x_values, y_values, c='blue', edgecolor='none', s=4)
plt.show()











