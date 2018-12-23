import sys #We are importing sys

sys.argv.pop(0) #We delete the first index, we don't need the script name.
A = list(map(int, sys.argv)) #We create a list, and map the arguments (that we get in string) to ints.

print(A) #We print out our arguments.
for j in range(len(A)): #We iterate over our numbers.
	key = A[j] #We set key to our current number.
	i = j - 1 #We create a variable to store the previous number's index.
	while i >= 0 and A[i] < key: #While the 'i' variable isn't 0 or greater, and the previous number is smaller than our number, do this loop. 
		A[i + 1] = A[i] #Set our number to the previous number.
		i = i - 1 #Decrease the 'i' variable.
	A[i + 1] = key #On 'i' + 1 index, we change the value to our current value.
print(A) #We print the sorted array/list.