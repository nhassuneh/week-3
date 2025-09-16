import seaborn as sns
import pandas as pd


# update/add code below ...
def fibonacci(n):
    """
    Compute the nth Fibonacci number using recursion with a helper function.

    Args:
        n (int): The index (non-negative) of the Fibonacci number to compute.
        
    Returns:
        int: The nth Fibonacci number.
    """
    def fib_inner(arr, count):
        # If we've reached the desired count, return the last number
        if count == n:
            return arr[-1]
        # Append next Fibonacci number to the array and remove the oldest
        arr.append(arr[-1] + arr[-2])
        arr.pop(0)
        # Recursive call with updated array and count
        return fib_inner(arr, count + 1)
    # Handling base cases, fib(0) = 0 and fib(1) = 1
    if n == 0:
        return 0
    if n == 1:
        return 1
    # Start with [0, 1] and count from 1
    return fib_inner([0, 1], 1)