"""
Let's start with the most simplest problem that can exist in Python.
Todo: Given three integers, return the largest integer.
"""


# solution one
def greatest_1(a, b, c):
    return max(a, b, c)


# solution two
def greatest_2(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    elif c > b and c > a:
        return c


# solution 3
def greatest_3(a, b, c):
    ...
