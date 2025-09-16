# TASK 3.2

# Write a generic function to checks passwords : they must contain more than 16 characters, at least 3 special character and 1 number.
# This function should be callable the following way:
# passcheck ( fun1 , 16 , " mysecretpassword " )
# passcheck ( fun2 , 3, " mysecretpassword " )
# passcheck ( fun3 , 1, " mysecretpassword " )

def fun1(y: int, password: str):
    return len(password) >= y

def fun2(y: int, word: str):
    characters = list(filter(lambda i: not i.isdigit() and not i.isalpha(), word))
    return len(characters) >= y

def fun3(y: int, word: str):
    digits = list(filter(lambda i: i.isdigit(), word))
    return len(digits) >= y

def passcheck(boo: callable, number: int, password: str):
    return boo(number, password)

print(passcheck(fun1, 16, "mysecretpassword"))
print(passcheck(fun2, 3, "mysecretpassword"))
print(passcheck(fun3, 1, "mysecretpassword"))