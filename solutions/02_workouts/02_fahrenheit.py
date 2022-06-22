"""
Fahrenheit
----------

Given an input `c` in Celsius as float, convert the temperature into Fahrenheit
and print out its value.

Input Format:
=============

The first line denotes `c`, temperature in Celsius

Output Format:
==============

Print the fahrenheit value

Constraints:
============

-273.15 <= s

Sample Input 0:
==============

0

Sample Output 0:
================

32.0
"""


def to_fahrenheit(c: float) -> float:
    """Covert Celsius to Fahrenheit"""
    f = (c * 9 / 5) + 32
    return f


t = float(input("Enter temperature in Celsius: "))

print(to_fahrenheit(t))
