"""
Todo: Write a Python program to count float number in a given mixed list.
"""


# solution one
def is_float_1(int_list):
    count = 0
    for item in int_list:
        if isinstance(item, float):
            count += 1
    return count


# solution two
def is_float_2(int_list):
    return len(list(filter(lambda x: isinstance(x, float), int_list)))


# solution three
def is_float_3(int_list):
    new_list = [x for x in int_list if isinstance(x, float)]
    return len(new_list)


# solution four
def is_float_4(int_list):
    count = 0
    for item in int_list:
        count += isinstance(item, float)
    return count
