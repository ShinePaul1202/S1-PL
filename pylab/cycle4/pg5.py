lst=[int(num) for num in input("enter list elements(space seperated):").split()]
powers_of_2 = list(map(lambda x: 2 ** x, lst))

print(f"\nPowers of 2: {powers_of_2}")
