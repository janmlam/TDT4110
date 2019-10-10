import math

def vector(a1, a2, a3):
	v = [a1, a2, a3]
	return v


def vprint(a1):
	print ("vector1 = [ %.2f, %.2f, %.2f ]" %(a1[0],a1[1],a1[2]))

def scalarVector(c, v):
	new_v = []
	var = 0
	i = 0
	while(i<3):
		var = c*v[i]
		new_v.append(var)
		i=i+1
	return new_v


def lengthVector(a):
	summ = 0
	for i in range(len(a)):
		summ = summ + (a[i])**2
	summ = math.sqrt(summ)
	return summ
	

def compare(c, a):
	print ("Length of a is: ", lengthVector(a))
	print ("Length of a*c is: ", lengthVector(scalarVector(c,a)))
	print ("Difference betwwen a and a*c is: ", abs(lengthVector(a)-lengthVector(scalarVector(c,a))))

def dotProduct(a, b):
	dotted = 0
	for i in range(len(a)):
		dotted = dotted + (a[i]*b[i])
	return dotted

print (dotProduct(vector(1,2,3), vector(3,2,1)))