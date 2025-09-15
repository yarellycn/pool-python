# TASK 2.1
# Write a snippet of code that prints all integers from 1 to 1000.

numbers = range(1,1001)

for number in numbers:
    print(number)

# TASK 2.2
#Prompt the user for a string. Display all the characters of this string twice.

print("Please insert a word.")

word = input()
newword = ""

for letter in word:
    newword += letter*2
print(newword)

# TASK 2.3
# Print all integers, decreasingly from 10 000 to 1, that are divisible by 7.

numbers = range(10000,0,-1)

for number in numbers:
    if number%7 == 0:
        print(number)

# TASK 2.4
# For all integers from -30 to 30:
# if it's a multiple of 3, display ”Fizz”
# if it's a multiple of 5, display ”Buzz”
# if it's a multiple of 3 and 5, display ”FizzBuzz”
# if it does not meet any of the previous conditions, just print the integer itself.

numbers = range(-30,31)

for number in numbers:
    if number%3 == 0 and number%5 == 0:
        print ("FizzBuzz")
    elif number%3 == 0:
        print("Fizz")
    elif number%5 == 0:
        print("Buzz")
    else:
        print(number)
    
# TASK 2.5
# Generate the lyrics of the song ”99 bottles of beer”.
# The song end when there is no more bottles on the wall.
# 1 bottle is singular...

numberofbottles = range(5,-1,-1)

for bottle in numberofbottles:
    if bottle > 2:
        print(bottle, "bottles of beer on the wall,")
        print(bottle, "bottles of beer.")
        print("If one of the bottles just happen to fall,")
        print(bottle-1, "bottles of beer on the wall.\n")
    elif bottle == 2:
        print(bottle, "bottles of beer on the wall.")
        print(bottle, "bottles of beer.")
        print("If one of the bottles just happen to fall,")
        print(bottle-1, "bottle of beer on the wall.\n")
    elif bottle == 1:
        print(bottle, "bottle of beer on the wall.")
        print(bottle, "bottle of beer.")
        print("If the bottle just happen to fall,")
        print(bottle-1, "bottles of beer on the wall.\n")
    else:
        print("No more bottles of beer on the wall,")
        print("no more bottles of beer.")
        print("Go to the store and buy some more,")
        print("99 bottles of beer on the wall...")