for i in range(1,10+1):
	print ("Multiplication table of: ", i)
	for j in range(1,10+1):
		print (i*j)
		j = j+1
	i=i+1

print ("")
for i in range(1,100+1):
	prime = True
	for j in range(2, i):
		if(i%j==0):
			prime = False
			break
	if(prime == True):
		print (i)