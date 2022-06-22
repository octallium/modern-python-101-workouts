"""
List Transformation
-------------------

Given an input two lists `n` and `m` of equal length and a transformation functions `f`,
apply `f` to the corresponding elements of `n` & `m`, save the result in new list
and print the transformed list.

List of functions `f`:

1. add
2. subtract
3. multiply
4. double

Constraints:
=============

length `n` == length `m`
function `f` receives two arguments `x` and `y` of type integer and returns an integer
after transforming it.

Output Format:
==============

Print a list with the transformed values

Sample Input 0:
==============

[1, 2, 3, 4, 5]
[4, 5, 6, 7, 8]

Sample Output 0:
================

[5, 7, 9, 11, 13]
[-3, -3, -3, -3, -3]
[4, 10, 18, 28, 40]
[10, 14, 18, 22, 26]
"""

from typing import Callable


def transform(
    nums_1: list[int],
    nums_2: list[int],
    func: Callable[[int, int], int],
) -> list[int]:
    """Transform the list using a transformer function"""
    nums: list[int] = []
    for i in range(len(nums_1)):
        nums.append(func(nums_1[i], nums_2[i]))
    return nums


def add(x: int, y: int) -> int:
    return x + y


# add: Callable[[int, int], int] = lambda x, y: x + y

subtract: Callable[[int, int], int] = lambda x, y: x - y
multiply: Callable[[int, int], int] = lambda x, y: x * y
double: Callable[[int, int], int] = lambda x, y: (x + y) * 2

n = [1, 2, 3, 4, 5]
m = [4, 5, 6, 7, 8]

print(transform(n, m, add))
print(transform(n, m, subtract))
print(transform(n, m, multiply))
print(transform(n, m, double))
