# TASK 3.1
# Ask the user his/her name and then greet him/her with ”Hello <Username>!”.
# Careful, only the first letter is capitalized, such as ”Hello Archibald!”.

print("Hello! What's your name?")
name = input()
Name = name.capitalize()
print("Hello " f"{Name} !")

# TASK 3.2
# Prompt the user for a number.
# Then, print the type of the provided input.

print("Please, insert a number.")
number = input()
print(type(number))

# TASK 3.3
# Prompt the user for two numbers.
# Then, print ”The sum of the provided numbers is <SUM>.”.

print("Please, enter two numbers")
    # METHOD 01
numbers = int(input()),int(input())
result = sum(numbers)
print("The sum of the provided number is", f"{result}"+".")

    # METHOD 02
print("Please, enter two numbers again.")
number1 = int(input())
number2 = int(input())
result = number1 + number2

print("The sum of the provided number is", f"{result}"+".")