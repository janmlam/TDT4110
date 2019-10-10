a = int(input("Type a number: "))
b = int(input("Type another number: "))

plus = a + b
times = a * b

if(plus > times):
	print ("a+b is larger than a*b:", plus)
else:
	print ("a*b is larger than a+b:", times)


number = int(input("What is 3 times 4? answer using a whole number: "))

if(number == 12):
	print ("you are certainly correct")
else:
	print ("wrong")
