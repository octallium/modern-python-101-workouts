"""
Odd or Even
-----------

Given an input of integer `n`, check and print if `n` is even or odd.

Input Format:
=============

The first line denotes `n`, an integer.

Output Format:
==============

Print if `n` is odd or even.

Sample Input 0:
==============

4

Sample Output 0:
================

4 is even
"""


def odd_or_even(num: int) -> None:
    """Check if num is odd or even"""
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")


num = int(input("Enter any number: "))
odd_or_even(num)
