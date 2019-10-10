

frequency = {}

def number_of_lines(filename):
	f = open(filename, "r")
	count = f.readlines()
	f.close()
	return len(count)

def number_frequency(filename):
	f = open(filename, "r") 
	f = f.read().split()
	#print (f)
	for line in f:
		if line not in frequency:
			frequency[line] = 1
		else:
			frequency[line] = frequency[line] +1
	print (frequency)

	for i, j in frequency.items():
		print ("%r: %r" %(i,j))


	



print(number_of_lines("numbers.txt"))
number_frequency("numbers.txt")