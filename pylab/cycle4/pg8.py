def compare(S1, S2, n):
    return S1[:n] == S2[:n]

S1 = input("Enter the first string: ")
S2 = input("Enter the second string: ")
n = int(input("Enter the number of characters to compare: "))

result = compare(S1, S2, n)
print("Result:", result)
