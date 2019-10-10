number_list = []

for i in range(0,100):
	number_list.append(i)

summ = 0

for i in number_list:
	if(i%3==0 or i%10==0):
		summ = summ + i

print (summ)


for i in range(0,len(number_list), 2):
	if(i!=number_list[-1]):
		number_list[i], number_list[i+1] = number_list[i+1], number_list[i]

reversed_list = []

for i in range(1,len(number_list)+1):
	reversed_list.append(number_list[-i])

print (reversed_list)