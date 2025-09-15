# TASK 2.1
# Write a recursive function that computes the sum of all integers from 1 to n, a given parameter.
# The parameter 42 should return 903.

n = 5

def factorial():
    if n == 0:
        return 1
    else :
        return n + (factorial(n))
