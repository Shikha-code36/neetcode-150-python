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
    def topKFrequent(self, nums, k):
        res={}

        for i in range(len(nums)):
            if nums[i] in res:
                res[nums[i]]+=1
            else:
                res[nums[i]]=1
        top_k = dict(Counter(res).most_common(k))
        return list(top_k.keys())
    
# Same as brute force but removing redundancy

'''
In this approach, we will first count the frequency of each element in the array using the Counter function.
Then, we will use the most_common function to get the k most frequent elements from the Counter object.
Finally, we will return the keys of the top_k dictionary as the output.
'''

class Solution:
    def topKFrequent(self, nums, k):
        top_k = Counter(nums).most_common(k)
        return [num for num,_ in top_k]

# Optimized Force
# Time Complexity: O(n)
# Overall Space Complexity: O(n)

'''
In this approach, we will first count the frequency of each element in the array and store it in the count dictionary.
Then, we will create a bucket of size n+1, where n is the length of the input array.
We will iterate through the count dictionary and append the elements to the bucket based on their frequency.
Finally, we will iterate through the bucket from the end and append the elements to the result array until we have k elements.
We will return the result array as the output.
'''

class Solution:
    def topKFrequent(self, nums, k):
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