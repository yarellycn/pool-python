#TASK 2.2
# Computes the value of 17 1024.

    #METHOD 01
print(17**1024)

    #METHOD 02
number1 = 17
number2 = 1024
result = number1**number2

print(f"{result}")

    #METHOD 3
number = 17
power = 1024
result = 1
#result1 = number*number
#result = result1*number
#result3 = result2*number
for i in range(power):
    result = result*number          # Is the same as result *= number

print(result)