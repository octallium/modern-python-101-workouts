"""
Contact
-------

Create a class `Contact` with two instance variables - `name` as string, `age` as int.

Input Format:
=============

Instance of Contact

Output Format:
==============

Print an instance of contact

Sample Input 0:
==============

c1 = Contact("Cece", 7)

Sample Output 0:
================

Cece 7
"""


class Contact:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def __repr__(self) -> str:
        return f"{self.name} {self.age}"

    def __str__(self) -> str:
        return f"{self.name} {self.age}"


c1 = Contact("Cece", 7)


print(c1)
