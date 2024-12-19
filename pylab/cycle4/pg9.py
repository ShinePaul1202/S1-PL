def add_integers(*args):
    """
    Returns the sum of all integer arguments.

    Parameters:
    *args: Integers to be added.

    Returns:
    int: The sum of the integers.
    """
    return sum(args)

print(add_integers(1, 2, 3))
print(add_integers(10, -5, 5))
print(add_integers(100, 200)) 
print(add_integers())
