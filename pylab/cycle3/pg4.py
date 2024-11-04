import math

def all_digits_even(number):
    for digit in str(number):
        if int(digit) % 2 != 0:
            return False
    return True

start = 1000
end = 9999
result = []

for i in range(start, end + 1):
    root = math.isqrt(i)
    if root * root == i and all_digits_even(i):
        result.append(i)

print("Four-digit numbers with all even digits that are perfect squares:", result)


