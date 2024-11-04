import math,cmath
print("Quadratic equation solver:ax^2 + bx + c = 0")
a = float(input("Enter coefficiant of x^2(a):"))
b = float(input("Enter coefficiant of x(b):"))
c = float(input("Enter constant value (c):"))

d = (b**2) - (4*a*c)
if d<0:
	sol1=(-b-cmath.sqrt((b**2)-4*a*c))/(2*a)
	sol2=(-b+cmath.sqrt((b**2)-4*a*c))/(2*a)

	print(f"the solution has complex solutions: {sol1} , {sol2}")
elif d==0:
	x=(-b)/(2*a)
	print(f"Equation has one solution:{x}")
else:
	sol1=(-b-math.sqrt(d))/(2*a)
	sol2=(-b+math.sqrt(d))/(2*a)
	print(f"Equation has two solutions : {sol1},{sol2}")
