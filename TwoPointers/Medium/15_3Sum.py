'''
15. 3Sum

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:
Input: nums = []
Output: []
Example 3:
Input: nums = [0]
Output: []
'''

# Brute Force
# Time Complexity: O(n^3)
# Space Complexity: O(m)

'''
In the brute force approach, we use three nested loops to iterate through all possible triplets in the array.
We check if the sum of each triplet is equal to zero and if it is, we add it to the result set.
The result set is used to avoid duplicates.
We convert the triplet to a tuple and add it to the set.
Finally, we convert the set back to a list of lists before returning it.
'''

class Solution:
    def threeSum(self, nums):
        res=set()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    if nums[i]+nums[j]+nums[k]==0:
                        res.add(tuple(sorted([nums[i],nums[j],nums[k]])))
        
        return [list(triplet) for triplet in res] 
    
# Two Pointers
# Time Complexity: O(n^2)
# Space Complexity: O(1) or O(n) depending on the sorting algorithm. O(m) for the result list.

'''
In the two pointers approach, we first sort the array.
Then we iterate through the array and for each element, we use two pointers to find the other two elements that sum to zero.
We set the left pointer to the next element and the right pointer to the last element.
We check if the sum of the three elements is equal to zero. If it is, we add it to the result list.
If the sum is greater than zero, we move the right pointer to the left. If the sum is less than zero, we move the left pointer to the right.
We also check for duplicates by skipping over elements that are the same as the previous element.
We continue this process until the left pointer is less than the right pointer.
'''

class Solution:
    def threeSum(self, nums):
        nums.sort()
        res=[]
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:  
                continue

            l=i+1
            r=len(nums)-1
            while l<r:
                crsum = nums[i]+nums[l]+nums[r]
                if crsum==0:
                    res.append([nums[i],nums[l],nums[r]])
                    l+=1
                    r-=1
                    while l<r and nums[l]==nums[l-1]:
                        l+=1
                    while l<r and nums[r]==nums[r+1]:
                        r-=1
                elif crsum>0:
                    r-=1
                else:
                    l+=1
        return res
    
sol = Solution()
nums = [-1,0,1,2,-1,-4]
print(sol.threeSum(nums))