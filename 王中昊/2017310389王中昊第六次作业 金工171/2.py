import csv
import pandas as pd
filen = ['pythonsign_20181030.csv',
            'pythonsign_20181113.csv',
            'pythonsign_20181009.csv']
label3 = ['注释','性别','院系','计算机名称','IP 地址','签到时间']
flag = 0
informations = []
for filename in filen:
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)
        for row in reader:
            for item in informations:
                if(row[1] == item['姓名']):
                    item['签到次数'] += 1
                    flag = 1
                    break
            if(flag == 0):   
                information = {}
                information['签到次数'] = 0
                for index, column_header in enumerate(header_row):
                    information[column_header] = row[index]
                    information['签到次数'] += 1
                for str in label3:
                    information.pop(str)
                informations.append(information)
            flag = 0            
info = pd.DataFrame(informations)
#print(info)
pd.DataFrame(informations).to_csv('签到次数.csv',encoding="utf-8-sig")
name = []
number = []
for item in informations:
    name.append(item['姓名'])
    number.append(item['签到次数'])
from matplotlib import pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False
fig = plt.figure(dpi=128, figsize=(100,6))
plt.scatter(name,number, c='blue')
plt.title("各个同学签到次数", fontsize=24)
plt.xlabel("姓名", fontsize=16)
plt.ylabel("签到次数", fontsize=16)
plt.tick_params(axis="both", which="major", labelsize=16)
plt.show()
