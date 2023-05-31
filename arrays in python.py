# -*- coding: utf-8 -*-
"""
Created on Wed May 31 20:39:06 2023

@author: ayesh
"""
def twoSum(nums, target):
    num_dict = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_dict:
            return [num_dict[complement], i]
        num_dict[num] = i
    return []

# Example usage
nums = [3,2,4]
target = 6
result = twoSum(nums, target)
print(result)

