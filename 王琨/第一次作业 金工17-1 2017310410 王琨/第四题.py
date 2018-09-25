prime_n=[];
a=2
for a in range(2,100):
    b=2
    for b in range(2,a):
        if a%b==0:
            break
    else:
        prime_n.append(a)
print(prime_n)
