import sys #We import sys

sys.argv.pop(0) #We delete the first index, we don't need the script name.
params = list(map(int, sys.argv)) #We create a list, and map the arguments (that we get in string) to ints.

v = params[0] #We set the 'v' variable to the value we want to search.
params.pop(0) #We drop the search value from the params list.
A = params #We set the 'A' variable to the value of the remaining params.
print(v) #We print the value we want to search for ('v' variable).
print(A) #We print the 'A' variable.
for j,k in enumerate(A): #We enumerate through our numbers.
	if A[j] == v: #If the current number is the searched one...
		i = j #we set the 'i' variable to it's index...
		break #and we break out of the loop.
	else: #If the current number isn't the searched one...
		i = "Couldn't find it" #we set it to an error string.
print(i) #We print the index or the error message.
if i != "Couldn't find it": #If the 'i' variable isn't the error message...
	print(i + 1) #Write out the actual position.
