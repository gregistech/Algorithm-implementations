A = [1,2,4,8,10,100,500,1000,5000,10000]
B = [0,4,1,4,23,50,250,500,500,10]
C = []
print(A)
print(B)
for n in range(len(A)):
	C.insert(n + 1, A[n] + B[n])
print(C)  