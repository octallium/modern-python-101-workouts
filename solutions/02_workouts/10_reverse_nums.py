"""
Reverse Num
-----------

Given an input of integer `n`, reverse and print the digits.

Constraints:
=============

Reverse the digits without converting them to string

Input Format:
=============

The first line denotes `n`, an integer.

Output Format:
==============

Print digits of `n` in reverse order.

Sample Input 0:
==============

1324

Sample Output 0:
================

4231
"""


def reverse(num: int) -> int:
    """Reverse digits of num"""
    to_reverse = num
    reversed_num = 0
    while to_reverse != 0:
        digit = to_reverse % 10
        reversed_num = reversed_num * 10 + digit
        to_reverse //= 10
    return reversed_num


num = int(input("Enter any number: "))
print(reverse(num))
