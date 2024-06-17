""" 1. Implement a function that checks whether a given string is a palindrome, 
but with the following constraints:

Avoid using any built-in string reversal functions (e.g., [::-1]).
Do not rely on external libraries or modules.
Students should create their own logic for checking palindromes."""

def palindrome(word):

    word_reverse=""
    for i in word:
        word_reverse=i+word_reverse
    
    if word == word_reverse:
        return True
    else:
        return False
        

    
word = input("Enter you word: " )
x = palindrome(word)

print(x)