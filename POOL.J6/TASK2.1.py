# TASK 2.1
# Write a recursive function that computes the sum of all integers from 1 to n, a given parameter.

def addintegrers(n):
    if n == 0:
        return 0
    else :
        return n + addintegrers(n-1)
    
print(addintegrers(42))

# fact(5) = 5 + fact(4)
# fact(4) = 4 + fact(3)
# fact(3) = 3 + fact(2)
# fact(2) = 2 + fact(1)
# fact(1) = 1 + fact(1)
# fact(0) = 0

# fact(5) = 5 + fact(4) = 5 + 10 = 15
# fact(4) = 4 + fact(3) = 4 + 6 = 10
# fact(3) = 3 + fact(2) = 3 + 3 = 6
# fact(2) = 2 + fact(1) = 2 + 1 = 3
# fact(1) = 1 + 0 = 1
# fact(0) = 0