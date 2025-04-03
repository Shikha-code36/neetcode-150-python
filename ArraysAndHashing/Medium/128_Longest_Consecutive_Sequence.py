'''
128. Longest Consecutive Sequence
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.

Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
Explanation: The longest consecutive elements sequence is [0, 1, 2, 3, 4, 5, 6, 7, 8]. Therefore its length is 9.
'''

# Brute Force Approach
# Time Complexity: O(nLogn)
# Space Complexity: O(n)

'''
In this approach, we first convert list to set to remove duplicates and then sort the list.
Then we iterate through the sorted list and check if the current element is equal to the next element + 1. If it is, we increment the count. 
If not, we check if the count is greater than the longest count and update it accordingly. Finally, we return the maximum of longest and count.
'''

class Solution:
    def longestConsecutive(self, nums):
        if len(nums)==0:
            return 0
        num= list(sorted(set(nums)))
        longest=1
        cnt=1
        for i in range(len(num)-1):
            if num[i]+1==num[i+1]:
                cnt+=1
            else:
                longest=max(longest,cnt)
                cnt=1
        return max(longest,cnt)
    
# Optimized Approach (using HashSet)
# Time Complexity: O(n)
# Space Complexity: O(n)

'''
In the below approach, we first convert the list to a set to remove duplicates.
Then we iterate through the set and check if the current number is the start of a sequence (i.e., if the previous number is not in the set).
If it is, we initialize a count and keep checking for the next consecutive numbers in the set until we reach the end of the sequence.
Finally, we update the longest count if the current count is greater than the longest count.
We return the maximum of longest and count.
'''
    
class Solution:
    def longestConsecutive(self, nums):
        if len(nums)==0:
            return 0
        num_set = set(nums)
        longest=0
        for num in num_set:
            if num-1 not in num_set:
                curren_num=num
                cnt=1
                
                while curren_num+1 in num_set:
                    cnt+=1
                    curren_num+=1
                    
                longest = max(longest,cnt)
        return max(longest,cnt)
                    
                
sol= Solution()
nums = [0,3,7,2,5,8,4,6,0,1]
print(sol.longestConsecutive(nums))