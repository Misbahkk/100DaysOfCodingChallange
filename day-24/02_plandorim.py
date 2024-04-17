"""Palindrome Check:
Write a function to check if a given string is a palindrome. 
The function should return True if the string is a palindrome and False otherwise. 
Ignore spaces and punctuation when checking."""

def plaindrome(word):
    
    def word_space(w):
        string = ''
        word_rever = []
        for char in w:
            if ' ' == char:
                continue
            elif char.isalpha():
                word_rever.append(char)
        word_reverse = string.join(word_rever)
        return word_reverse
    return word_space(word)


    
    
def reverse_word(word): 
    word1 = plaindrome(word) 
    reverse_word = word1[::-1]



    if word1 == reverse_word:
        return True
    else:
        return False


pla_string = reverse_word("m @am ")

print(pla_string)

