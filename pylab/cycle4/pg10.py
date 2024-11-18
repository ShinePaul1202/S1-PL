import math

def permutations(n, r):
    return math.factorial(n) // math.factorial(n - r)

def combinations(n, r):
    return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))

n = int(input("Enter total number of objects (n): "))
r = int(input("Enter number of objects taken at a time (r): "))

print(f"P({n}, {r}) = {permutations(n, r)}")
print(f"C({n}, {r}) = {combinations(n, r)}")
