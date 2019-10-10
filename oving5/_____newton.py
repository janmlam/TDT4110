import math

def f(x):
	fx = (x-12)*(math.e)**(5*x)-8*(x+2)**2
	return fx

def g(x):
	gx = -x-2*(x)**2-5*(x)**3+6*x**4
	return gx

def derivate(h, x, func):
	var = (((func((x+(h/2)))-(func((x-(h/2))))))) / h
	return var


def newtons_method(h, x, func, tol):
	xk = x
	xk1 = 0

	while(abs(xk1-xk)<tol):
		
		xk1 = xk - (func(x))/(derivate(h,x,func))







print (derivate(0.000001,-2,f))