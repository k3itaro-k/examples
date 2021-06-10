""" 
Palindrome


This function takes a string/number and prints if it is palindrome or not.

"""
import re


def palindrome(word):
    clean_word = re.sub('[^a-zA-Z0-9]','',word).lower()
    anti_word = clean_word[::-1]

    if clean_word == anti_word:
        print(f'"{word}"" is palindrome.')
    else:
        print(f'"{word}" is not palindrome.')


if __name__=='__main__':
    a = 'Never odd or even.'
    palindrome(a)