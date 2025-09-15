# TASK 1.5
# Add a parameter to provide the possibility for veg sandwich (double vegetables + no ham).
# If this option isn't specified, the sandwich must be a lettuce-tomato-double ham one by default.

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

def vegburguer():
    (bread())
    for i in range(2):
        (lettuce(), tomato())
    (bread())

def prepare(number: int, veggie = False):
    if type(number) == float:
        print("I can't do this!")
    elif type(number) == str:
        print("I can't do this!")
    elif number < 0:
        print("I can't do this!")
    elif number > 0:
        for i in range(number):
                if veggie == True:
                    vegburguer()
                else: 
                    burguerdoubleham()

prepare(1, veggie=True)