# TASK 2.1
# Write a recursive function that computes the sum of all integers from 1 to n, a given parameter.

def addintegrers(n):
    if n == 0:
        return 0
    else :
        return n + addintegrers(n-1)
    
print(addintegrers(42))

# fact(0) = 0
# fact(1) = 1
# fact(2) = 3
# fact(3) = 6
# fact(4) = 10
# fact(5) = 15