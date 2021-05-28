"""
todo: Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]). Return the running sum of nums.
"""


# solution 1
def running_sum_1(nums):
    for i in range(1, len(nums)):
        nums[i] += nums[i - 1]
    return nums


# solution 2
def running_sum_2(nums):
    total = 0
    result = []
    for x in nums:
        total = total + x
        result.append(total)
    return result

