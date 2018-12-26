import sys #We import sys

sys.argv.pop(0) #We delete the first index, we don't need the script name.
A = list(map(int, sys.argv)) #We create a list, and map the arguments (that we get in string) to ints.

print(A) #We print out our arguments.
for j,k in enumerate(A): #We enumerate through our numbers.
	min_element = min(A[j:]) #We set the variable to the smallest number from the current index.
	min_index = A[j:].index(min_element) #We get it's index.
	A[j + min_index] = A[j] #We push the number.
	A[j] = min_element #We set it to the new number.
print(A) #We print out the result.
