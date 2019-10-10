import random

ranNum = random.randint(1,100)
guess = 0

while(guess != ranNum):
	guess = int(input("guess a number: "))
	if(guess < ranNum):
		print ("The correct number is higher")
	elif(guess > ranNum):
		print ("The correct number is lower")
	else:
		print ("You guessed correct, the number was: ", ranNum)
