import random

def randList(size, lower, upper):
	list1 = []
	for i in range(size+1):
		list1.append(random.randint(lower,upper))
	return list1

def compareList(list1, list2):
	