def product(n, tol):
	new_sum = 1
	old_sum = 1
	count = 0
	for i in range(1,n+1,):
		count = count + 1 
		something = (1 +(1/(i)**2))
		old_sum = new_sum
		new_sum = new_sum*something
		print (old_sum, new_sum)
		#print (abs(new_sum-old_sum))
		if((abs(new_sum-old_sum))<tol):
			print ("Tol: ", tol) 
			print ("The product was: ", new_sum, "after ", count, " iterations.")
			return


product(50, 0.01)

