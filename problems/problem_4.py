"""
todo: Given a positive number `num`, write a function which returns True if num is a perfect square else False.
"""
from math import sqrt

# solution 1
def is_sq_1(num):
    for i in range(num):
        if i * i == num:
            return True
    return False


# solution 2
def is_sq_2(num):
    return (num ** 0.5).is_integer()


# solution 3
def is_sq_3(num):
    if num == 1:
        return True
    left = 1
    right = num
    while left <= right:
        mid = (left + right) // 2
        if mid * mid == num:
            return True
        elif mid * mid < num:
            left = mid + 1
        else:
            right = mid - 1
    return False


# solution 4
def is_sq_4(num):
    num_list = str(num ** 0.5).split('.')
    if len(num_list[1]) == 1:
        return True
    else:
        return False

