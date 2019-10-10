
def all_applied(filename):
	f = open(filename, "r", encoding="utf-8")
	counter = 0
	for i in f.readlines():
		if "Alle" in i:
			counter +=1
	return counter


def average(filename):
	counter = 0
	ave = 0
	f = open(filename, "r", encoding="utf-8")
	for i in f.readlines():
		if "NTNU" in i:
			if "Alle" not in i:
				g = i.split(",")
				counter +=1
				ave += float(g[-1])
	return (ave/counter)

def lowest(filename):
	default  = 100.
	name = ""
	f = open(filename, "r", encoding="utf-8")
	for i in f.readlines():
		if "Alle" not in i:
			j = i.split(",")
			if(float(j[-1])<default):
				default = float(j[-1])
				name = j[0]
	return name




print(all_applied("2011.csv"))
print(average("2011.csv"))
print(lowest("2011.csv"))