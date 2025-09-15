#TASK 3.1
# Prompt the user for a clear message and a key. Then, use Caesar cipher to encrypt the clear message with the key. Finally, print the encrypted message.

alphabet = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")

print("Insert a word to crypt and a key")

word, key = input().split()
key = int(key)

for letter in word:
    wordposition = alphabet.index(letter)
    finalwordposition = wordposition + key
    print(alphabet[finalwordposition%26], end="")
print("")

# TASK 3.2
# Write a program that can decrypt any Caesar-ciphered text.

print("Insert a crypted word and it's key")

word, key = input().split()
key = int(key)

for letter in word:
    wordposition = alphabet.index(letter)
    finalwordposition = wordposition - key
    print(alphabet[finalwordposition%26], end="")
print("")