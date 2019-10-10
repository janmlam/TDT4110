from math import sin

x = float(input("Choose value for x: "))
h = float(input("Choose value for h: "))

#h = float(10**-3)
#x = float(3.14)

f1 = sin(x)
f2 = sin((x+h))

devOfSinx = (f2-f1) / (h)

print (devOfSinx)
