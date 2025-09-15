# CHALLENGE
# Write a little program that computes the power function as fast as possible.
# How long does your program takes to compute 42**84? and 42***168 ?
# You are not allowed to use the system function.

import time
startingTime = time.time()

base = 42
power = 84
result = 1

for i in range(power):
    result = result * base

print(result)

duration = time.time()-startingTime
print(duration)