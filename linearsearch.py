import sys

sys.argv.pop(0)
params = list(map(int, sys.argv))

v = params[0]
params.pop(0)
A = params
print(v)
print(A)
for j in range(len(A)):
	if A[j] == v:
		i = j;
		break
	else: 
		i = "Couldn't find it"
print(i)
if i != "Couldn't find it":
	print(i + 1)