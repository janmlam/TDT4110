def load_bin(filename):
	asd = ""
	try:
		f = open(filename, "r+")
	except:
		print ("Error: Could not open file", filename)
		return
	for stuff in f.readlines():
		asd = asd+stuff.strip()
	print (asd)
	return asd


#load_bin("123.txt")

def bin_to_dec(binary):
	counter = 0
	bina = 2
	if(len(binary) == 0):
		if(binary[0]=="1"):
			return 1
		else:
			return 0
	new = binary[::-1]
	for i in range(l):
		if(i==0):
			if(new[i]=="1"):
				counter += 1
		if(new[i]=="1"):




