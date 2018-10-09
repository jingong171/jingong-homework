shu=list(range(1,2001))
print("1-2000之间的完数：")
for i in shu :
    yinzihe = 0
    for j in range(1,i):
        if i%j == 0:
            yinzihe = yinzihe + j
    if yinzihe == i:
                print(i)
