# TASK 1.5
# Prompt the user for an integer:
# if it's 42, display ”a” ;
# if it's smaller or equal than 21, display ”b” ;
# if it's even, display ”c” ;
# if this integer divided by 2 is smaller than 21 (excluded), display ”d” ;
# finally, if it's is odd and greater or equal than 45, display ”e” ;
# in any other cases, display ”f”.

print("Please insert a number.")
number = int(input())

    # METHOD 01
if number == 42:
    print("a")
elif number <= 21:
    print("b")
elif number%2 == 0:
    print("c")
elif number/2 < 21:
    print("d")
elif number%2 != 0 and number >= 45:
    print("e")
else:
    print("f")

    # METHOD 02
print("Please insert a number.")
number = int(input())

if number == 42:
    print("a")
if number <= 21:
    print("b")
if number%2 == 0:
    print("c")
if number/2 < 21:
    print("d")
if number%2 != 0 and number >= 45:
    print("e")
if (number == 42 or number <= 21 or number%2 == 0 or number/2 < 21 or (number%2!= 0 and number >= 45)) == False:
    print("f")