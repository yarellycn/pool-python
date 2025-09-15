print("Please, write a sentence.")
text = input()
everyword = text.split()
newword = ""

for word in everyword:
    newword += word[0]
print(newword)