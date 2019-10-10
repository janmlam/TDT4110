def gcd(a, b):
	old_b = 0
	while(b>0):
		old_b = b
		b = a%b
		a = old_b
	#print (a)
	return a


def reduce_fraction(x, y):
	divisor = gcd(x,y)
	new_x = x/divisor
	new_y = y/divisor
	#print (new_x, new_y)
	return new_x, new_y

b=4

while(True):
	a = int(input("a=? "))
	print (gcd(a,b))
	#b = int(input("b=? "))
	#var1, var2 = reduce_fraction(a, b)
	#print ("For a:",a," b:",b," the output is:",var1,"/",var2)

#reduce_fraction(4, 2)
#reduce_fraction(42, 13)


