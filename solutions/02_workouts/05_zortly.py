"""
Zortly
------

Given an input of string `s`, replace the first alphabet with 'Z' and add 'ly' to 
the back of the string and print the new word

Input Format:
=============

The first line denotes `s`, a string.

Output Format:
==============

Print the input string `s` with the correct format

Sample Input 0:
==============

Octallium

Sample Output 0:
================

Zctalliumly
"""


def zortly(word: str) -> str:
    new_word = "Z" + word[1:] + "ly"
    return new_word


word = input("Enter any word: ")

print(zortly(word))
