r = 0.5 #float((input("r=? ")))
n = 15 #int(input("n=? "))
tol = 0.001 #float((input("tol=? ")))
sum1 = 0
i=0
tol_count = 0
while(i<=n):
	rx = r**(i)
	sum1 = sum1 + rx
	print (sum1)
	tol_count = tol_count+1
	if((2-sum1)<tol):
		print ("within tol limit")
		break
	i = i+1
#11 instead of 12 ?????
print ("The loop ran ", tol_count, " times to be within the limit: ", tol)
print ("Difference between the given, and estimated value is: ", 2-sum1)