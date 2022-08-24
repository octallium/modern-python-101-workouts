"""
Vector
-------

Create a class `Vector` with one instance variable `args`. Instantiate the class `Vector`
by accepting variable number of integer or float values.

Implement the following methods on class Vector:

1. Addition. Returns a new vector.
2. Subtraction. Returns a new vector.
3. Multiplication. Returns a new vector.
4. Floor Division. Returns a new vector.
5. True Division. Returns a new vector.
6. Equal
7. Less than or equal
8. More than or equal
9. Make the class iterable

Input Format:
=============

Instance of Vectors

Sample Input 0:
==============

v1 = Vector(-3, 4, 7)
v2 = Vector(5, 6, 7)

print(v1)
print(len(v1))
print(bool(v1))
print(bool(v2))
print(v1 + v2)
print(v1 - v2)
print(v1 * v2)
print(v1 / v2)
print(v1 // v2)
print(v2 == Vector(5, 6, 7))
print(v1 < v2)
print(v1 > v2)
print(v1 <= v2)
print(v1 >= v2)
print("4" in v1)


Sample Output 0:
================

Vector(-3, 4, 7)
3
True
True
Vector(2, 10, 14)
Vector(-8, -2, 0)
Vector(-15, 24, 49)
Vector(-0.6, 0.6666666, 1.0)
Vector(-1, 0, 1)
True
True
False
True
False
False
-3 4 7
"""
