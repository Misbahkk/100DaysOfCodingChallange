"""Anagram Detection:
Write a function to check if two given strings are anagrams of each other. 
Anagrams are strings that contain the same characters in a different order. 
The function should return True if the strings are anagrams and False otherwise."""


def anagram_detection(word1,word2):
    word1 = word1.lower().replace(" ","")
    word2 = word2.lower().replace(" ","")

    return sorted(word1) == sorted(word2)







words = anagram_detection("Misbah","asiMbh")
print(words)