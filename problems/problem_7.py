"""
todo: Given a list of n-D with each element as an integer, write a program to return the sum of all integer.

"""
from functools import reduce


def n_sum_1(nd_list):
    return sum(map(sum, nd_list))


def n_sum_2(nd_list):
    total = 0
    for item in nd_list:
        total += sum(item)
    return total


def n_sum_3(nd_list):
    total = 0
    for lst in nd_list:
        for item in lst:
            total += item
    return total

