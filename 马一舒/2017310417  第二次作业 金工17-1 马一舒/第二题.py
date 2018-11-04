m=25
n=15
S=[]
R=[]
for s in range (25,376):
    if s%m==0 and s%n==0:
        S.append(s)
print("m,n的最小公倍数："+ str(min(S)))
for r in range(1,26):
    if m%r==0 and n%r==0:
        R.append(r)
print("m,n的最大公约数："+ str(max(R)))
