# TASK 1
# Create a list that contains 5 numbers and print the first one.
# Your code must be functional whichever number of elements the list contains.
list = [22, 7, 97, 1, 2, 93]

# TASK 2
# Display the last element of your list.
print(list[-1])

# TASK 3
# Add a 6th element in your list.
list.append(12)

# TASK 4
# Display all the elements of your list.

    # METHOD 1
print(list)

    # METHOD 2
for number in list:
    print(number)

# TASK 5
# Delete the last element and display all the remaining elements.
# Your code must be functional whichever number of elements the list contains.
list.pop()
print (list)

# TASK 6
# Add an element at the beginning of the list and display all its elements.
list.insert(0,4)
print(list)

# TASK 7
# Display the substring from the 2nd to the 5th elements. Can you do it in one line?
print(list[1:4])

# TASK 8
# Reverse the list by creating a new list with the same elements, but starting from the end.
# Display all the elements of this new list.

list2 = list[::-1]
print(list2)

# TASK 9
# Display one element out of two of the list.
print(list2[::2])

# TASK 10
# Add 17 elements at the end of your list. Please, do not do it in 17 lines. . .

    # METHOD 1
itemstoadd = [i for i in range(1,18)]       # Je recup chaque i de mon for in range pour que ca sort comme une liste

list2.extend(itemstoadd)
print(list2)

    # METHOD 2
list2 += [i for i in range(1,18)] 
print(list2)

# TASK 11
# What does the following code make? 
# Error will be shown bc the method is "extend" not "extends". If "extend", it will merge the 2 lists. CORRECT
# my_first_list = [4,5,6]
# # my_second_list = [1,2,3]
# my_first_list.extends(my_second_list)

my_first_list = [4,5,6]
my_second_list = [1,2,3]
my_first_list.extend(my_second_list)
print(my_first_list)

# Same with:
# * will extract every item on the list referred. The merge of the 2 list will be shown.
my_first_list = [7, 8, 9]
my_second_list = [4, 5, 6]
my_first_list = [*my_first_list, *my_second_list]
print(my_first_list)

test = [*"coucou"]
print(test)