'''
238. Product of Array Except Self

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.
 

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
'''

# Brute Force (Inbuilt math function approach)
# Time Complexity: O(n^2)
# Space Complexity: O(n)

import math

class Solution:
    def productExceptSelf(self, nums):
        result=[]

        for i in range(len(nums)):
            new_arr = nums[:i] + nums[i+1:]
            res=math.prod(new_arr)
            result.append(res)
        return result
    

# Brute Force (Without using inbuilt math function)
# Time Complexity: O(n^2)
# Space Complexity: O(n)       

'''
In this approach, we will iterate through the array and for each element, we will calculate the product of all elements except the current element.
We will store the result in the result array and return it.
'''

class Solution:
    def productExceptSelf(self, nums):
        result=[]

        for i in range(len(nums)):
            prod=1
            for j in range(len(nums)):
                if i!=j:
                    prod*=nums[j]
            result.append(prod)
            
        return result
    
# Optimized Approach
# Time Complexity: O(n)
# Space Complexity: O(n)

'''
In this approach, we will first calculate the prefix product of the array by iterating from right to left and store it in an array pref[].
Then we will calculate the suffix product of the array by iterating through left to right and store it in an array suff[].

Finally, we will calculate the product of pref[i]*suff[i] for each element of the array and store it in the result array.
'''
class Solution:
    def productExceptSelf(self, nums):
        n=len(nums)
        prod=[1]*n
        pref=[1]*n
        suff=[1]*n
        
        prefix=1
        
        for i in range(n):
            pref[i]=prefix
            prefix*=nums[i]
            
        suffix=1
        
        for i in range(n-1,-1,-1):
            suff[i]=suffix
            suffix*=nums[i]
            
        for i in range(n):
            prod[i]=pref[i]*suff[i]
        
        return prod
    
# Optimized Approach
# Time Complexity: O(n)
# Space Complexity: O(1)

'''
This approach calculates the product of all elements except nums[i] using two passes:

Prefix Pass (left to right) stores the product of all elements before nums[i].

Suffix Pass (right to left) multiplies it with the product of all elements after nums[i].
This achieves O(n) time and O(1) extra space by updating the result in-place. 
'''

class Solution:
    def productExceptSelf(self, nums):
        n=len(nums)
        prod=[1]*n
        
        prefix=1
        
        for i in range(n):
            prod[i]=prefix
            prefix*=nums[i]
            
        suffix=1
        
        for i in range(n-1,-1,-1):
            prod[i]*=suffix
            suffix*=nums[i]
        
        return prod
                

            
            
obj = Solution()
nums = [1,2,4,6]
print(obj.productExceptSelf(nums))