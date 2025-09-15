# TASK 01
# Create a list of 10 numbers.
# Print the result of the multiplication of all elements of this list.

list1 = [i for i in range(1,11)]
result = 1

for n in list1:
    result *= n

print(result)

# TASK 02
# Test this code and try to explain it: [x + 10 for x in [3, 2, 6, 7, 1, 4]]
#  Ca va recuperer chaque item de la liste et va aditionner 10. CORRECT

list2 = [x + 10 for x in [3, 2, 6, 7, 1, 4]]
print(list2)

# TASK 03
# Test this code and try to explain it: list(map(lambda x: x * x, [3, 2, 6, 7, 1, 4])
# Lambda is a function that will be applied: map will allow lambda to apply it to every item in the list; list will make a list of the results. CORRECT

list3 = list(map(lambda x: x*x, [3, 2, 6, 7, 1 , 4])) 
print(list3)

# TASK 04
# Browse the list and display both the smallest and the biggest elements.

    # METHOD 01
smallest = min(list3)
biggest = max(list3)

print(smallest, biggest)

    # METHOD 02
minmax = [min(list3),max(list3)]

print(minmax)

    # METHOD 03
smallest = list3[0]
biggest = list3[0]

for x in list3:
    if x > biggest:
        biggest = x

for x in list3:
    if x < smallest:
        smallest = x

print(smallest, biggest)

# TASK 05
# Display all the elements smaller than 7.
smallerthan7 = filter(lambda x: x<7, list3)
print(list(smallerthan7))

# TASK 06
# Sort your list in descending order.
    #Sorting in ascending order
list3.sort()

print(list3)

    #Sorting in descending order
list3.sort(reverse = True)

print(list3)

# TASK 07
# Test this code and try to explain it:
list4 = [x // 2 if x % 2 == 0 else x * 2 for x in [42, 3, 4, 18, 3, 10]]

    # I will divide by 2 if an item from [42, 3, 4, 18, 3, 10] is even. Otherwise, I will multiply it by 2.
    # Output : 21, 6, 2, 9, 6, 5 CORRECT

print(list4)

# TASK 08
# Test this code and try to explain it:
list5 = list(filter(lambda x: x > 10, [42, 3, 4, 18, 3, 10]))

    # I will show all the numbers that are greater than 10 from [42, 3, 4, 18, 3, 10].
    # Output : 42, 18 CORRECT

print(list5)

# TASK 09
# Test this code and try to explain it:
list6 = [*enumerate([42, 3, 4, 18, 3, 10])]

    # I will add a counter to each item of the list.
    # Output : [(0, 42), (1, 3), (2, 4), (3,18), (4, 3), (5, 10)] CORRECT

print(list6)

# TASK 10
# Test this code and try to explain it:
first_name = ["Jackie", "Bruce", "Arnold", "Sylvester"]
last_name = ["Stallone", "Schwarzenegger", "Willis", "Chan"]
magic = [*zip(first_name, last_name[::-1])]

    # list last_name will be reversed
    # zip will combine the list making tuples according to their position. The * will make them a list of tuples.
    # Output of magic : [('Jackie', 'Chan'), ('Bruce', 'Willis'), ('Arnold', 'Schwarzenegger'), ('Sylvester', 'Stallone')] CORRECT

print(magic[0])             # I will print the truple in index 0 of the list:       ('Jackie', 'Chan')                          CORRECT
print(magic[3])             # I will print the truple in index 3 of the list.       ('Sylvester', 'Stallone')                   CORRECT
print(magic[1][0])          # I will print the truple in index 1 and 0 of the list. ('Bruce', 'Willis'), ('Jackie', 'Chan')     INCORRECT: I will print the truple in index 1, then print the item in index 0 in the truple.
print(magic[0][1])          # I will print the truple in index 0 and 1 of the list. ('Jackie', 'Chan'), ('Bruce', 'Willis')     INCORRECT: I will print the truple in index 0., then print the item in index 1 in the truple.
print(magic[2])             # I will print the truple in index 2 of the list.       ('Arnold', 'Schwarzenegger')                CORRECT