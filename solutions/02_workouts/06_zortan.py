"""
Zortan
------

Given an input of string `s`, reverse the first two and last two characters.
Minimum input length should be 4, otherwise throw a Value Error.

Input Format:
=============

The first line denotes `s`, a string.

Constraint:
===========

length s >= 4

Output Format:
==============

Print the input string `s` with the correct format

Sample Input 0:
==============

crystal

Sample Output 0:
================

rcystla
"""


def zortan(word: str) -> str:
    """Convert to Zortan"""
    if len(word) < 4:
        raise ValueError("Word needs to be atleast 4 characters long")

    first_2 = list(word[:2])
    first_2.reverse()

    last_2 = list(word[len(word) - 2 :])
    last_2.reverse()

    middle = word[2 : len(word) - 2]

    new_word = "".join(first_2) + middle + "".join(last_2)
    return new_word


# def zortan_2(word: str) -> str:
#     if len(word) < 4:
#         raise ValueError("Word needs to be atleast 4 characters long")

#     a, b = word[0], word[1]
#     c, d = word[-2], word[-1]
#     new_word = b + a + word[2 : len(word) - 2] + d + c
#     return new_word


# def zortan_3(word: str) -> str:
#     if len(word) < 4:
#         raise ValueError("Word needs to be atleast 4 characters long")

#     return word[:2][::-1] + word[2 : len(word) - 2] + word[-2:][::-1]


word = input("Enter any word: ")

print(zortan(word))
# print(zortan_2(word))
# print(zortan_3(word))
