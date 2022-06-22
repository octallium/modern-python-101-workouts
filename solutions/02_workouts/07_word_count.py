"""
Word Count
----------

Count number of unique words.

Given an input of string `s`, convert the string into dictionary with keys of unique
words in `s` and value equal to the number of their occurrences, ignore counting spaces.

Input Format:
=============

The first line denotes `s`, a string.

Output Format:
==============

Print the dictionary with correct keys & values.

Sample Input 0:
==============

The sun and the moon

Sample Output 0:
================

{'the': 2, 'sun': 1, 'and': 1, 'moon': 1}
"""


def word_count(sentence: str) -> dict[str, int]:
    """Count number of unique words"""

    words = sentence.lower().split()
    count: dict[str, int] = {}
    for word in words:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
    return count


sentence = input("Enter a sentence: ")
print(word_count(sentence))
