"""
Count Words
-----------

Given an input of string `s`, count and print the number of words.

Input Format:
=============

The first line denotes `s`, a string.

Output Format:
==============

Print the count as integer

Sample Input 0:
==============

The sky is blue

Sample Output 0:
================

4
"""


def count_words(sentence: str) -> int:
    """Count num of words in a string"""
    words = sentence.split()
    count = len(words)
    return count


s = input("Enter a sentence: ")

print(count_words(s))
