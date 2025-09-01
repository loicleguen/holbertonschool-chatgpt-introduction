#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function Description:
        Calculate the factorial of a number recursively.
    
    Parameters:
        n (int): A non-negative integer whose factorial is to be calculated.
    
    Returns:
        int: The factorial of the number n. Returns 1 if n is 0.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Convert the first command-line argument to an integer
# and calculate its factorial
f = factorial(int(sys.argv[1]))

# Print the result
print(f)
