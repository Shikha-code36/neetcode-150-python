'''
1. Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
'''

# Solution Brute Force
# Time Complexity: O(n^2)
# Space Complexity: O(1)

'''
In the below approach, we used two for loops to iterate through the array and check if the sum of the two numbers is equal to the target.
If it is, we return the indices of the two numbers.
'''

class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

# Solution Using Hashing
# Time Complexity: O(N)
# Space Complexity: O(N)

'''
This approach uses a dictionary to store the difference between the target and the current number as the key and the index as the value.
We then iterate through the array and check if the current number is in the dictionary.
If it is, we return the index of the current number and the value of the dictionary.
'''

class Solution:
    def twoSum(self, nums, target):
        prev = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in prev:
                return [prev[diff], i]
            prev[nums[i]] = i


