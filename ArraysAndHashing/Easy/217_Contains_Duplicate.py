'''
217. Contains Duplicate

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:
Input: nums = [1,2,3,1]
Output: true

Example 2:
Input: nums = [1,2,3,4]
Output: false

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true

Constraints:
1 <= nums.length <= 105
-109 <= nums[i] <= 109
'''

# Brute Force 1
# Time Complexity: O(n^2)
# Space Complexity: O(1)

'''
This approach uses two for loops to iterate through the array and check if any two numbers are equal.
If they are, we return True, else we return False.
'''

class Solution:
    def containsDuplicate(self, nums):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]==nums[j]:
                    return True
        return False
    
# Brute Force 2 (Using Sorting)
# Time Complexity: O(nlogn)
# Space Complexity: O(1)

'''
Below approach sorts the array and then checks if any two consecutive numbers are equal.
If they are, we return True, else we return False.
'''

class Solution:
    def containsDuplicate(self, nums):
        if len(nums)==1:
            return False
        nums.sort()
        for i in range(len(nums)):
            if nums[i-1]==nums[i]:
                return True
        return False
    

# Optimal Solution (Using Hashing)
# Time Complexity: O(n)
# Space Complexity: O(n)

'''
In the below approach, we used a dictionary to store the count of each number in the array.
If the number is already present in the dictionary, we return True, else we add the number to the dictionary.
Finally, we return False.
'''

class Solution:
    def containsDuplicate(self, nums):
        hash={}

        for i in range(len(nums)):
            if nums[i] in hash:
                return True
            else:
                hash[nums[i]]=1
        return False

# Optimal Solution (Using Set)
# Time Complexity: O(n)
# Space Complexity: O(n)

'''
This approach uses a set to store the numbers in the array.
If the length of the set is not equal to the length of the array, we return True, else we return False.
'''

class Solution:
    def containsDuplicate(self, nums):
        return len(nums)!=len(set(nums))


obj = Solution()
print(obj.containsDuplicate([1,2,3,4,1]))