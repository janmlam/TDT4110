def f(k):
	f_current = 0
	f_next = 1
	sum1 = 0

	for i in range(0, k):
		print (f_current)
		sum1 = sum1 + f_current
		temp = f_current
		f_current = f_next
		f_next = temp + f_next
	print ("Sum of the first", k, "fibonacci numbers is: ", sum1)

k = int(input("kth number of fibonacci? "))

f(k)

