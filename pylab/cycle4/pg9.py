def add_integers(*args):
    """
    This function takes a variable number of integer arguments and returns their sum.
    
    Parameters:
    *args (int): The integers to be summed up.

    Returns:
    int: The sum of all the integer arguments.
    
    Example:
    >>> add_integers(1, 2, 3)
    6
    >>> add_integers(5, 10, 15, 20)
    50
    """
    return sum(args)

result = add_integers(1, 2, 3)
print("Sum of numbers:", result)  

result = add_integers(5, 10, 15, 20)
print("Sum of numbers:", result)  
