word = str(input("type a hidden word: "))
lifes = int(input("type a number of lifes: "))

while True:
	guess = str(input("guess a letter: "))
	if(guess in word):
		print("the guessed letter is in the hidden word \nyou have: ", lifes, "lifes left")
	else:
		print("the guessed letter is not in the hidden word")
		lifes = lifes - 1

	if(lifes == 0):
		print("no more lifes")
		break