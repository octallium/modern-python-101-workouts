"""
Add Numbers
-----

Prompt user to enter two integers and print its sum.

Sample Input:
============

3
4

Sample Output:
=============

7

"""


def add_nums(num1: int, num2: int) -> int:
    """Add and return the sum of two numbers"""
    return num1 + num2


num1 = int(input("Please enter a number: "))
num2 = int(input("Please enter another number: "))

print(add_nums(num1, num2))
