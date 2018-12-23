import sys

sys.argv.pop(0)
A = list(map(int, sys.argv))

print(A)
for j,k in enumerate(A):
	min_element = min(A[j:])
	min_index = A[j:].index(min_element)
	A[j + min_index] = A[j]
	A[j] = min_element
print(A)
