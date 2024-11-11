num_terms = int(input("Enter the number of terms for powers of 2: "))

powers_of_2 = list(map(lambda x: 2 ** x, range(num_terms)))

print(f"Powers of 2 up to {num_terms} terms: {powers_of_2}")
