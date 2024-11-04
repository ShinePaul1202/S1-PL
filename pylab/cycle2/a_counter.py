names=[]
n=int(input("Enter limit:"))
for i in range(n):
	el=input(f"Enter name{i+1} :")
	names.append(el)
print("Occurances of ‘a’ in names:")
for name in names:
	print(f"{name}:{name.lower().count('a')}")
