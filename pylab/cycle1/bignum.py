a=int(input("Enter the 1st number:"))
b=int(input("Enter the 2nd number:"))
c=int(input("Enter the 3rd number:"))
if a>b and a>c:
 largest=a
elif b>c and b>a:
 largest=b
else:
 largest=c
print("The largest number is :",largest)
