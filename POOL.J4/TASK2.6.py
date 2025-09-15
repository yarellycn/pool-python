# TASK 2.6
# Write a program that takes an integer n as input. 
# Then, for each integer from 2 to n/2, display the list of its multiples strictly smaller than n, in descending order.

# n = int(input())

# test=[1,2,3]
# test.reverse()
# print(test)

n = 14
start = 2
end = (n // 2)  

for number in range(start, end+1):                          # [2,3,4,5,6,7]
    for multiplier in range((n - 1) // number, 0, -1):      # [6, 5, 4, 3, 2, 1]
        print(number*multiplier, end=" ")
    print("")