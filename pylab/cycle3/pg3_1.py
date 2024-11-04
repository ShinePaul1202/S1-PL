def fact(n):
	if n==0 or n==1:
		return 1
	elif n<0:
		return -1
	else:
		return n*fact(n-1)
n=int(input("enter number:"))
if fact(n)==-1:
	print("enter positive number")
else:
	f=fact(n)
	print("factorial:",f)
