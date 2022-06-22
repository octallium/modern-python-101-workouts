"""
Character Count
---------------

Count number of unique characters.

Given an input of string `s`, convert the string into dictionary with keys of unique
characters in `s` and value equal to the number of their occurrences, ignore counting spaces.

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

{'t': 2, 'h': 2, 'e': 2, 's': 1, 'u': 1, 'n': 3, 'a': 1, 'd': 1, 'm': 1, 'o': 2}
"""


def count_characters(sentence: str) -> dict[str, int]:
    """Count number of unique characters"""
    characters = list(sentence.lower())
    count: dict[str, int] = {}
    for character in characters:
        if character == " ":
            continue
        if character in count:
            count[character] += 1
        else:
            count[character] = 1
    return count


sentence = input("Enter a sentence: ")
print(count_characters(sentence))
