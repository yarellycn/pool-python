# TASK 1.1

# (42 > 12)                    42 is greater than 12 -> true
# (12 = 12)                    variable "12" is 12 -> true ????
# ("hello" == "world")         "hello" equals "world" -> false
# (218 >= 118)                 218 is greater/equal to 118 -> true
# ("a".upper() == "A")         "a".upper() equals A -> true
# (1*2*3*4 <= 9)               1*2*3*4 is minor/equal to 9 -> false
# ("z" in "azerty")            z is present in the string azerty -> true

#TASK 1.2
# Ask an integer to the user. If it's equal to 42, display ”This is correct!”.
print("Please, insert a number.")
number = int(input())

if number == 42:
    print("This is correct!")

#TASK 1.3
# Prompt the user for an integer. Then, if it is:
# odd, display ”This integer is odd” ;
# even, display ”This integer is even”.
print("Please, insert a number.")
number = int(input())

if number%2 == 0:
    print("This integer is even.")
else: 
    print ("This integrer is odd.")

# TASK 1.4
print("Please, write the magic words to open the door.")
text = input()

if text == "open sesame":
    print("Access granted.")
elif text == "Will you open, you goddamn!":
    print("Access fucking granted.")
else:
    print("Permission denied.")