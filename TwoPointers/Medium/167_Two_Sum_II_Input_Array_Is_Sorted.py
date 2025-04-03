'''
167. Two Sum II - Input Array Is Sorted

Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number.
Return the indices of the two numbers, index1 and index2, such that index1 < index2.
You must write an algorithm that runs in O(n) time complexity.

Example 1:
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]

Explanation: Because numbers[0] + numbers[1] == 9, we return [1, 2].

Example 2:
Input: numbers = [2,3,4], target = 6
Output: [1,2]
'''

# Brute Force
# Time Complexity: O(n^2)
# Space Complexity: O(1)

'''
Below is the brute force solution.
It uses two nested loops to check all pairs of numbers in the array.
If a pair is found that sums to the target, it returns their indices.
'''

class Solution:
    def twoSum(self, numbers, target):
        for i in range(len(numbers)):
            for j in range(i+1,len(numbers)):
                if numbers[i]+numbers[j]==target:
                    return [i+1,j+1]
        return []
    

# Two Pointers
# Time Complexity: O(n)
# Space Complexity: O(1)

'''
Below is the two pointers solution.
It uses two pointers, one starting at the beginning of the array and the other at the end.
The pointers move towards each other until they find a pair of numbers that sum to the target.
If a pair is found, it returns their indices.
If the sum is less than the target, the left pointer is moved to the right.
If the sum is greater than the target, the right pointer is moved to the left.
'''

class Solution:
    def twoSum(self, numbers, target):
        i=0
        j=len(numbers)-1
        
        while i<=j:
            if numbers[i]+numbers[j]==target:
                return [i+1,j+1]
            elif numbers[i]+numbers[j]> target:
                j-=1
            else:
                i+=1
        return []
    
obj = Solution()
numbers = [1,2,3,4]
target = 3
print(obj.twoSum(numbers, target))
# Output: [1,2]
        