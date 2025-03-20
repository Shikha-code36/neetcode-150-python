'''
49. Group Anagrams

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.

Example 2:

Input: strs = [""]

Output: [[""]]

Example 3:

Input: strs = ["a"]

Output: [["a"]]


Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
'''

# Brute Force
# Total Complexity: O(N log N + N K log K)
# Space Complexity: O(N K)

class Solution:
    def groupAnagrams(self, strs):
            new_val = sorted(strs)
            mapp={}
            for key, value in enumerate(new_val):
                vals = sorted(value)
                val = "".join(vals)
                if val in mapp:
                    mapp[val].append(new_val[key]) 
                else:
                    mapp[val]=[new_val[key]]
                    
            return list(mapp.values())
    
# Optimized Solution
# Time Complexity: O(m*n)
# Space Complexity: O(m)

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        return list(res.values())

obj=Solution()
strs=["act","pots","tops","cat","stop","hat"]
print(obj.groupAnagrams(strs))
    