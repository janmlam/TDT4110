def price(age):
	if(age<5):
		return 0
	elif(age<=20):
		return 20
	elif(age<=25):
		return 50
	elif(age<=60):
		return 80
	else:
		return 0




print (price(int(input("Input your age: "))))