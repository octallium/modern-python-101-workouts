"""
Wordly
------

Given an input of string `s`, add 'ly' to the back of the string and
print the new word

Input Format:
=============

The first line denotes `s`, a string.

Output Format:
==============

Print the input string `s` with `ly` added to the back

Sample Input 0:
==============

Octobot

Sample Output 0:
================

Octobotly
"""


def wordly(word: str) -> str:
    """Adds `ly` to the end of the string"""
    new_word = word + "ly"
    return new_word
    # return f"{word}ly"


word = input("Enter any word: ")

print(wordly(word))