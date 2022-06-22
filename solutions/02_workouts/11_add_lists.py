"""
Add Lists
---------

Given an input two lists `n` and `m` of equal length, add the elements of `n`
with the corresponding elements of `m` and print the output.

Constraints:
=============

length `n` == length `m`

Input Format:
=============

The first line denotes `n`, list of integers.
The second line denotes `m`, list of integers.

Output Format:
==============

Print a list with the added values

Sample Input 0:
==============

1 2 3 4 5
4 5 6 7 8

Sample Output 0:
================

[5, 7, 9, 11, 13]
"""


def add_list(nums_1: list[int], nums_2: list[int]) -> list[int]:
    """Add two lists"""
    nums: list[int] = []
    for i in range(len(nums_1)):
        nums.append(nums_1[i] + nums_2[i])
    return nums


input_1 = input("Enter the first list: ")
n = list(map(int, input_1.split()))

input_2 = input("Enter the second list: ")
m = list(map(int, input_2.split()))


print(add_list(n, m))
