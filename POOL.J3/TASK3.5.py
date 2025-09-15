text = "Write a program that counts the frequency of each letter from a given text and infers the language of this very text."
splittext = list(text.lower())

for letter in splittext:
    ascii = ord(letter)
    if (ascii >= ord("a") and ascii <= ord("z")) or ((ascii >= 223 and ascii <= 255) and ascii != 247):
        print("valid char:", letter)
    else:
        print("invalid char:", letter)

