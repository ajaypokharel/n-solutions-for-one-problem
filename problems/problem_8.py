"""
todo: You are given a string s. Return the reversed strong.

Example: 'pythonHub'
Result: 'buHnohtyp'
"""


def reverse_1(s):
    reversed_s = ''
    for i in range(len(s)-1, -1, -1):
        reversed_s += s[i]
    return reversed_s


def reverse_2(s):
    return s[::-1]
