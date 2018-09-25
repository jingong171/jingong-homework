m = 22
n = 99

for i in range(1,min(m,n)+1):
    if n%i==0 and m%i==0 :
        greatest=i
print("The greatest commom divisor is "+str(greatest)+".")

common_multiples = []
for j in range(max(m,n),m*n+1):
    if j%m==0 and j%n==0 :
        common_multiples.append(j)
        lowest = min(common_multiples)
print("The lowest common multiple is "+str(lowest)+".")


        

