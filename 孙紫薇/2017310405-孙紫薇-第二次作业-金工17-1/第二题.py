Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> m=6
>>> n=4
>>> #M中为公约数，N中为部分公倍数
>>> M=[]
>>> N=[]
>>> for p in range(1,7):
	if n%p==0 and m%p==0:
		for q in range(4,25):
			if q%m==0 and q%n==0:
				M.append(p)
				N.append(q)
				print(M)
				print(N)

				
[1]
[12]
[1, 1]
[12, 24]
[1, 1, 2]
[12, 24, 12]
[1, 1, 2, 2]
[12, 24, 12, 24]
>>> max(M)
2
>>> min(N)
12
>>> 
