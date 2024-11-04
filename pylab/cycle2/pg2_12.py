lst1=[int(num) for num in input("Enter first list(space separated):").split()]
lst2=[int(num) for num in input("Enter second list(space separated):").split()]

lenght=len(lst1)==len(lst2)
lsum=sum(lst1)==sum(lst2)
common=set(lst1)&set(lst2)

if lenght:
	print("lists lenghts are same")
else:
	print("lists lenght are not same")

print(f"lists common elements{common}")

if lsum:
	print("list sums are same")
else:
	print("list sums are not same")
