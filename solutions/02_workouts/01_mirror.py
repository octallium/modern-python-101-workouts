"""
Mirror
------

Given an input `s` of string, print out its mirror image.

Input Format:
=============

The first line denotes `s` which is the object to be mirrored

Output Format:
==============

Print the mirror image of `s`

Sample Input 0:
==============

Chiko

Sample Output 0:
================

okihC
"""


def mirror(to_mirror: str) -> str:
    values = list(to_mirror)
    values.reverse()

    return "".join(values)
    # return to_mirror[::-1]


to_mirror = input("What do you want to mirror? ")

print(mirror(to_mirror))
