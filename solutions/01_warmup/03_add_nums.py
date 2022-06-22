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

# SOLUTION 1 -


def add_nums(num1: int, num2: int) -> int:
    """Add and return the sum of two numbers"""
    return num1 + num2


num1 = int(input("Please enter a number: "))
num2 = int(input("Please enter another number: "))

print(add_nums(num1, num2))


# SOLUTION 2 -


# def add_nums(num1: int, num2: int) -> int:
#     """Add and return the sum of two numbers"""
#     return num1 + num2


# def get_nums() -> tuple[int, int]:
#     """Get valid integers from user"""
#     while True:
#         try:
#             num1 = int(input("Please enter 1st number: "))
#             num2 = int(input("Please enter 2nd number: "))
#             break
#         except ValueError as e:
#             print("Please enter only integer values")
#     return num1, num2


# # num1, num2 = get_nums()
# # print(add_nums(num1, num2))

# print(add_nums(*get_nums()))
