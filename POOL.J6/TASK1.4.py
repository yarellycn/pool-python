# TASK 1.4
# Write a function that:
# Takes the number of sandwiches to prepare as a parameter ;
# Then displays as many sandwiches as requested.

def bread():
    print("<//////////>")

def lettuce():
    print("~~~~~~~~~~~~")

def tomato():
    print("O O O O O O")

def ham ():
    print("============")

def burguerdoubleham():
    (bread(), lettuce(), tomato(),)
    for i in range(2):
        (ham())
    (bread())

def prepare(number: int):
    if type(number) == float:
        print("I can't do this!")
    elif type(number) == str:
        print("I can't do this!")
    elif number < 0:
        print("I can't do this!")
    elif number > 0:
        for i in range(number):
            burguerdoubleham()

prepare(-2)