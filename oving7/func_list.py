import random
from statistics import mode

random_numbers = []

for i in range(101):
	random_numbers.append(random.randint(1,10))
"""
count = 0
for i in range(len(random_numbers)):
	if(random_numbers[i] == 2):
		count = count+1
"""



print ("Sum: ", sum(random_numbers))
print ("Amount of 2s: ", random_numbers.count(2))
new = sorted(random_numbers)
print ("Sorted: ", new)
print ("Most appeared number:", mode(new))
print ("reversed: ", new[::-1])
#ny variabel med reversed(new) / list.reverse()

