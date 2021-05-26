"""
todo: Write a Python program to add the sum of every digit in a given integer.
"""
from functools import reduce


# solution one using reduce
def add_sum_1(num):
    return reduce(lambda x, y: int(x) + int(y), str(num))


# solution two using simple iteration
def add_sum_2(num):
    total = 0
    for item in str(num):
        total += int(item)
    return total


# solution using list pop() method
def add_sum_3(num):
    total = 0
    new_list = list(str(num))
    while not new_list == []:
        total += int(new_list.pop())
    return total


# solution using simple list comprehension and sum built-in function
def add_sum_4(num):
    return sum([int(item) for item in str(num)])
