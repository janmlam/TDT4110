a = float(input("Choose a value for a: ")) 
b = float(input("Choose a value for b: ")) 
c = float(input("Choose a value for c: ")) 

d = (b**2) - 4*a*c

if(d<0):
	print ("The eq. : ", a, "x^2 + ", b, "x +", c, "= 0 has two imgainal solutions.")
elif(d>0):
	print ("The eq. : ", a, "x^2 + ", b, "x +", c, "= 0 has two real number solution.")
else:
	print ("The eq. : ", a, "x^2 + ", b, "x +", c, "= 0 has a solution with doubleroot.")

