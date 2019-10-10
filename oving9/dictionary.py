my_family = {}

def add_family_member(role, name):
	add_new = True
	for i in my_family.keys():
		if(i == role):
			my_family[role].append(name)
			add_new = False
	if(add_new == True):
		my_family[role] = [name]
		#my_family[role].append(name)


add_family_member("bror","kappa")
add_family_member("sos","kappa")
add_family_member("far","kappa")
add_family_member("far","kappa2")


print(my_family)

