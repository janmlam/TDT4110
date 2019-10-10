def bubble_sort(list1):
	for k in range(len(list1)):
		for i in range(len(list1)):
			if(i != len(list1)-1):
				if(list1[i]>list1[i+1]):
					list1[i], list1[i+1] = list1[i+1], list1[i]
	return list1
	
"""
def selecetion_sort(l1):
	new = []
	l1 = sorted(l1)
	l1 = l1[::-1]
	for i in range(len(l1)):
		new.append(l1[0])
		l1.pop(0)
	return new, l1
"""

def selecetion_sort(l1):
	new = []
	for i in range(len(l1)):
		max_value = max(l1)
		max_ele = l1.index(max_value)
		new.insert(0, max_value)
		l1.pop(max_ele)
	return new, l1

asd = [76,4,1,2,6,5]

print (bubble_sort(asd))
print (selecetion_sort(asd))
