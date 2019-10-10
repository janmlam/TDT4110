def wholeNumber(number):
	if ((number.is_integer()) == True):
		print ("This is a whole number")
		return True
	else:
		print ("This is not a whole number")
		return False


def evenNumber(number):

	return (number%2) == 0
	#if (number%2) == 0:
	#	print ("This is an even number")
	#	return True
	#else:
	#	print ("This is not an even number")
	#	return False


def pnNumber(number):
	return number > 0

	#if number > 0:
	#	print ("This is a positive number")
	#	return True
	#else:
#		print ("This is a negative number")
#		return False


a = float(input("Say a number: "))
wholeNumber(a)
pnNumber(a)

b = float(input("Say another number: "))
wholeNumber(b)
evenNumber(b)
pnNumber(b)


def compareNr(num1, num2):
	return not (num1 != num2)
	#if(num1 != num2):
	#	print ("Number 1 and number 2 is not alike")
	#	return False
	#else:
	#	print ("Number 1 and number 2 is alike")
	#	return True

