# TASK 2.2
#  Write a recursive function that prompt the user for a string of characters, strip out the spaces and punctuation signs, lowercase the string, then test if is a palindrome.

import string

def isitpalindrome(launch):
    print("Please insert a sentence. (Don't forget the puntuation signs!)")
    phrase = input()
    phrase_min = phrase.lower()
    phrase_noesp = phrase_min.replace(" ", "")
    phrase_clean = "".join(filter(lambda x : x not in string.punctuation, phrase_noesp))
    phrase_lenght = (len(phrase_clean))- 1

    def palindrome(phrase_clean:str, i):
        if i == (phrase_lenght)//2:
            return True
        if phrase_clean[i] == phrase_clean[phrase_lenght-i]: 
            return palindrome(phrase_clean,i+1)
        else :
            return False
    
    print(palindrome(phrase_clean, 0))

isitpalindrome("launch")