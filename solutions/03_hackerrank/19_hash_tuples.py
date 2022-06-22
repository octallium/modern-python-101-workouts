"""
Task
----

Given an integer `n`, and space-separated integers as input, create a tuple, `t`, of 
those integers. Then compute and print the result of hash(t)

Note: hash() is one of the functions in the __builtins__ module, so it need not be imported.

Input Format:
=============

The first line contains an integer, denoting the number of elements in the tuple.
The second line contains space-separated integers describing the elements in tuple `t`

Output Format:
==============

Print the result of hash(t)

Sample Input 0:
==============

2
1 2

Sample Output 0:
================

3713081631934410656
"""

nums_str = input().strip().split()

# nums = [int(x) for x in values_str]
nums = map(int, nums_str)
hashed_value = hash(tuple(nums))

print(hashed_value)
