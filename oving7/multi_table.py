def separate(numbers, threshold):
	list_1 = []
	list_2 = []
	for i in range(len(numbers)):
		if(numbers[i] < threshold):
			list_1.append(numbers[i])
		else:
			list_2.append(numbers[i])
	return list_1, list_2


a = [1,2,3,4,5,6]
print (separate(a, 3))


def multiplication_table(n):
	list_123 = []
	for i in range(n):
		temp = []
		for j in range(n):
			temp.append((i+1)*(j+1))
		list_123.insert(i, temp)
	return list_123



print(multiplication_table(4))

