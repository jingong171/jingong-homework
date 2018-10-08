#求3、6、9直到30的平方和
answer=0
for unit in range(3,31,3):
    answer+=unit**2
print(answer)
