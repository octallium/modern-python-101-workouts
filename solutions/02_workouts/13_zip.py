"""
Zip Lists
---------

Given an input two lists `n` and `m` of equal length, group the corresponding elements
together in a tuple and add to a list. Print the zipped list of tuples.

Constraints:
=============

length `n` == length `m`
Do not use the built-in zip function.

Input Format:
=============

List of integers, `n` and `m`

Output Format:
==============

Print a list with the zipped values

Sample Input 0:
==============

[1, 2, 3, 4, 5]
[4, 5, 6, 7, 8]

Sample Output 0:
================

[(1, 4), (2, 5), (3, 6), (4, 7), (5, 8)]
"""


def zipper(nums_1: list[int], nums_2: list[int]) -> list[tuple[int, int]]:
    """Zip the lists"""
    nums: list[tuple[int, int]] = []
    for i in range(len(nums_1)):
        nums.append((nums_1[i], nums_2[i]))
    return nums


n = [1, 2, 3, 4, 5]
m = [4, 5, 6, 7, 8]

print(zipper(n, m))

print(list(zip(n, m)))
