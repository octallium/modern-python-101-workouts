"""
Sort Contacts
-------------

1. Create a class `Contact` with two instance variables - `name` as string, `age` as int.
2. Create four instances of `Contact` and add them to a list `l`.
3. Create a function `sort` which takes 2 arguments and returns a sorted list. First argument
   list `l` of Contacts and second argument boolean value to denote if the list is to be sorted
   in reverse order or not.
4. Sort list `l` with age and print the list in ascending and descending order

Input Format:
=============

List of Contacts

Output Format:
==============

Print sorted list with ascending and descending values

Sample Input 0:
==============

c1 = Contact("Cece", 7)
c2 = Contact("Niko", 8)
c3 = Contact("Louis", 13)
c4 = Contact("Kiro", 4)

contacts = [c1, c2, c3, c4]

Sample Output 0:
================

[Kiro 4, Cece 7, Niko 8, Louis 13]
[Louis 13, Niko 8, Cece 7, Kiro 4]
"""

from typing import Callable


class Contact:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def __repr__(self) -> str:
        return f"{self.name} {self.age}"

    def __str__(self) -> str:
        return f"{self.name} {self.age}"


c1 = Contact("Cece", 7)
c2 = Contact("Niko", 8)
c3 = Contact("Louis", 13)
c4 = Contact("Kiro", 4)

contacts = [c1, c2, c3, c4]

sort_func: Callable[[Contact], int] = lambda contact: contact.age

contacts.sort(key=sort_func)
print(contacts)

contacts.sort(key=sort_func, reverse=True)
print(contacts)
