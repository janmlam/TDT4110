def write_to_file(data):
	f = open("kappa.txt", "a")
	f.write(data)
	f.close()
	return data


def read_from_file(filename):
	f = open(filename, "r")
	text = f.read()
	f.close()
	print (text)



def main():
	var = input("Do yo uwant to read or write?")
	if(var == "write"):
		toWrite = input("What do you want to write?")
		asd = write_to_file(toWrite)
		print (asd, "was written to file")
	elif(var == "read"):
		read_from_file("kappa.txt")
	elif(var == "done"):
		print ("You're done")
		return
	else:
		print("Please use write, read, or done as command")
	main()
	

main()



#with open("filename.txt, "w") as f: 
	#>asdasdasd
