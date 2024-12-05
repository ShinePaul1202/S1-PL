def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        result = 1
        for i in range(2, num + 1):
            result *= i
        return result

def sum_series(n):
    total = 0
    for i in range(1, n + 1):
        total += (i ** i) / factorial(i)  # n^n / n!
    return total

n = int(input("Enter the value of n: "))

result = sum_series(n)

print(f"The sum of the series up to {n} terms is: {result}")

