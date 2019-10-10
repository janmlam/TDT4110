def check_equal(s1, s2):
	list1 = list(s1)
	list2 = list(s2)
	if(len(list1) != len(list2)):
		return False
	for i in range(len(list1)):
		if(list1[i] != list2[i]):
			return False
	return True

def reversed_word(str):
	list1 = list(str)
	new = []
	for i in range(len(list1)):
		new.insert(i, list1[(len(list1)-1-i)])
	return ("".join(new))


def check_palindrome(str):
	if(check_equal(str, reversed_word(str)) == True):
		return True
	else:
		return False


def contains_string(str1, str2):
	list1 = list(str1)
	list2 = list(str2)
	len_1 = len(list1)
	len_2 = len(list2)

	for i in range(len_1-len_2):
		test1 = []
		for j in range(len_2):
			test1.append(list1[i+j])
		if(check_equal(test1, list2) == True):
			return i
		print (test1)
	return -1
			#print (i+j, j)




print (check_equal("hei", "hei på deg"))
#print (reversed_word("Morna Jens"))
#print (check_palindrome("agnes i senga"))
print (contains_string("pepperkake", "per"))
print (contains_string("pepperkake", "ola"))