# TASK 3.3
# Add error handling to your previous function.
# A common misuse would be providing input of the wrong type (integer, boolean, string, ...).

def fun1(y: int, password: str):
    return len(password) >= y

def fun2(y: int, word: str):
    characters = list(filter(lambda i: not i.isdigit() and not i.isalpha(), word))
    return len(characters) >= y

def fun3(y: int, word: str):
    digits = list(filter(lambda i: i.isdigit(), word))
    return len(digits) >= y

def passcheck(boo, number: int, password: str):
    if not callable(boo):
        print("Error : boo parameter is not a callable.")
        return
    if type(number) is not int:
        print("Error : number parameter is not an integer.")
        return
    if type(password) is not str:
        print("Error : password parameter is not a string.")
        return
    if number < 0:
        print("Error : number can't be negative.")
    if password == "":
        print("Error : password is empty.")
        return
    return boo(number, password)

print(passcheck(fun1, 16, "mysecretpassword"))
print(passcheck(fun2, 3, "mysecretpassword"))
print(passcheck(fun3, 1, "mysecretpassword"))