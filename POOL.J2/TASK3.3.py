#TASK 3.3
# Write a snippet of code that calculates the sum of the digits of 123434565.
# Use the same code to calculates the sum of the digits of 345567426, then 44490320097.

    #METHOD 01
number = 12345
result = 0
while number > 0:
    result = result + (number % 10)
    number = number // 10

print(result)

    #METHOD 02
def task (number:int):
    result=0
    for nb in str(number):
        result = result + int(nb)
    return result

print(task(12345))

test=12.34
print(int(test))


result=""
for digit in str(test):
    print(f" - digit = {digit}")
    if digit == ".":
        print("j'ai trouve un point donc je sors")
        break
    result = result + digit
    print(f" - result = {result}")
print(result)



def getIntegerPart(nb:float):
    result=""
    for digit in str(nb):
        if digit == ".":
            break
        result = result + digit
    return result

integer_part=getIntegerPart(98523.2832)
print(integer_part)

nb=1
test=(nb == 1)

should_add=True
#boolean
#bool
#bool-et-un
if should_add:
    #blabla
    print("toto")
    should_add=False
else:
    print("toto")
    should_add=True
    #blabla