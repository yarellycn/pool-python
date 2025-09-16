# TASK 3.1
# Write 3 functions, each taking a string s and an integer n as parameters and returning a boolean:
# funA checks if s contains at least n characters;
# funB checks if s contains at least n special characters;
# funC checks if s contains at least n numbers.

# def char(word: str, y: int):
#     word_lenght = len(word)
    
#     if word_lenght >= y:
#         return True
#     else:
#         return False              # All this is the same as:

def char(word: str, y: int):
    return len(word) >= y

def spc_char(word: str, y: int):
    characters = list(filter(lambda i: not i.isdigit() and not i.isalpha(), word))
    return len(characters) >= y

def digit(word: str, y: int):
    digits = list(filter(lambda i: i.isdigit(), word))
    return len(digits) >= y

print(char("Hello!@/123", 4))
print(spc_char("Hello!@/123", 4))
print(digit("Hello!@/123", 4))