# TASK 2.6
# Write a snippet of code that prints 10 times a given string.

text = "Butterfly"

    # METHOD 01
method1 = text*10
print(method1)

    # METHOD 02
def method2(text):
    for i in range(10):
        print(text)

method2("Fly")

    # METHOD 03
method3 = ""
for i in range(10):
    method3 += "Fly away"
print(method3)