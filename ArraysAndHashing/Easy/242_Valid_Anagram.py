'''
242. Valid Anagram

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Constraints:
1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
'''

# Brute Force
# Time Complexity: O(nlogn)
# Space Complexity: O(n)

'''
In this approach, we will sort both the strings and iterate through sorted strings. If elements are not equal, then return False, else return True.
'''

class Solution:
    def isAnagram(self, s, t):
        if len(s)!=len(t):
            return False

        s1=sorted(s)
        t1=sorted(t)

        for i,j in zip(s1,t1):
            if i!=j:
                return False
        return True
        
# Solution 2
# Time Complexity: O(nlogn)
# Space Complexity: O(n)

'''
In this approach, we will sort both the strings and compare them. If they are equal, then return True, else return False.
'''

class Solution:
    def isAnagram(self, s, t):
        if len(s)!=len(t):
            return False

        return sorted(s)==sorted(t)

# Solution 3
# Time Complexity: O(n)
# Space Complexity: O(1) (or O(n) for large character sets)

'''
This approach uses a dictionary to store the count of characters in both strings. 
If the count of characters in both strings is equal, then return True, else return False.
'''

class Solution:
    def isAnagram(self, s, t):  
        count_s = {}
        count_t = {}

        for i in range(len(s)):
            count_s[s[i]] = count_s.get(s[i], 0) + 1
            count_t[t[i]] = count_t.get(t[i], 0) + 1
        return count_s==count_t
    
# Solution 4
# Time Complexity: O(n)
# Space Complexity: O(1) (or O(n) for large character sets)

'''
This approach uses inbuilt Counter function to store the count of characters in both strings.
If the count of characters in both strings is equal, then return True, else return False.
'''

from collections import Counter

class Solution:
    def isAnagram(self, s, t):
        return Counter(s)==Counter(t)

obj = Solution()
s="racecar"
t="carrace"
print(obj.isAnagram(s,t))