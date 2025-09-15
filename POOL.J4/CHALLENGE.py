print("Write a number and a word")

number, word = input().split()

if number == 0:
    quit()

def isVowel(x):
    if (x == 'a' or x == 'e' or x == 'y' or
        x == 'i' or x == 'o' or x == 'u'):
        return True
    return False

vowels = list(filter(isVowel,word))

if len(vowels) != 0:
    print(number)

if int(number) >= 42:
    print(number)
else:
    print(word)

# def evenOnly(nb: int):
#     return nb % 2 == 0


# def myfilter(predicate: callable, iterable: iter):
#     result = []
#     for i in iterable:
#         if predicate(i) == True:
#             result.append(i)
#     return result

# def mymap(predicate: callable, iterable: iter):
#     result = []
#     for i in iterable:
#         result.append(predicate(i))
#     return result


# print(myfilter(lambda x: x > 10, [30, 8, 28, 3, 6, 9, 10, 15]))
# print(myfilter(evenOnly, [30, 8, 28, 3, 6, 9, 10, 15]))

# print(mymap(lambda x: x + 2, [1, 4, 2, 9]))