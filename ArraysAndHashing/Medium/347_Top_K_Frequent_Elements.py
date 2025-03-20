'''
347. Top K Frequent Elements

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
 

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
'''
# Brute Force
# Time Complexity: O(n + n log k) = O(n log k)
# Overall Space Complexity: O(n)

from collections import Counter

class Solution:
    def topKFrequent(nums, k):
        res={}

        for i in range(len(nums)):
            if nums[i] in res:
                res[nums[i]]+=1
            else:
                res[nums[i]]=1
        top_k = dict(Counter(res).most_common(k))
        return list(top_k.keys())

# Brute Force
# Time Complexity: O(n)
# Overall Space Complexity: O(n)


class Solution:
    def topKFrequent(nums, k):
        count={}
        
        buck = [[] for i in range(len(nums)+1)]

        
        for num in nums:
            count[num]= 1+count.get(num,0)
        for key, value in count.items():
            buck[value].append(key)
            
        res=[]
        for i in range((len(buck)-1), 0, -1):
            for j in buck[i]:
                res.append(j)
                if len(res)==k:
                    return res
                
obj = Solution()

nums = [1,1,1,2,2,3]
k = 2

print(obj.topKFrequent(nums, k))