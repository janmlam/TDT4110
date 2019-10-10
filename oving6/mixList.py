
def isSixAtEdge(list):
	if(list[0] == 6 or list[-1] == 6):
		return True
	else:
		return False


def average(list):
	summ = sum(list)
	gj = summ /len(list)
	return gj


def median(list):
	sort = sorted(list)
	print (sort)
	mediann = (len(list)/2)-0.5
	mediann = int(mediann)
	return sort[mediann]

