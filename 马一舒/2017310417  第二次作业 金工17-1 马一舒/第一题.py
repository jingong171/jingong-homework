digits=[]
for a in range(1,11):
    digit=3*a
    digits.append(digit)
squares=[digit**2 for digit in digits]
print(str(sum(squares)))

