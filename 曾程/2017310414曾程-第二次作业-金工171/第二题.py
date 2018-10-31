m=218
n=545
common_divisor=[]
for i in range(1,218):
    if m%i==0 and n%i==0:
        common_divisor.append(i)
        continue
greatest_common_divisor=max(common_divisor)
print("The greatest common dividor is "+str(greatest_common_divisor)+".")

common_multiple=[]
for i in range(1,218):
    for j in range(1,545):
        if m*j==n*i:
            common_multiple.append(m*j)
            continue
least_common_multiple=min(common_multiple)
print("The least common multiple is "+str(least_common_multiple)+".")
