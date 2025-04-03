'''
271. Encode and Decode Strings

Design an algorithm to encode and decode strings. The encoding and decoding should be reversible.
The encoded string should be able to be decoded back to the original string.
Implement the Solution class:

Example 1:

Input: ["neet","code","love","you"]

Output:["neet","code","love","you"]
Example 2:

Input: ["we","say",":","yes"]

Output: ["we","say",":","yes"]
Constraints:

0 <= strs.length < 100
0 <= strs[i].length < 200
strs[i] contains only UTF-8 characters.


'''

# Brute force approach
# Time Complexity: O(n) for encoding and O(n) for decoding
# Overall Space Complexity: O(n)

'''
The idea is to use a delimiter to separate the strings when encoding and decoding. 
We can use a special character that is not present in the strings to separate them.
We can use the '#' character as a delimiter.
We can encode the strings by concatenating them with the delimiter and then decoding them by splitting the concatenated string using the delimiter.
'''

class Solution:
    
    def encode(self, strs):
        val=""
        new_s=""
        for s in strs:
            new_s=str(len(s))+"#"+s
            val+=new_s
        return val


    def decode(self, s):
        res = []
        i = 0
        
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
            
        return res

    
solution = Solution()

strs = ["neet", "code", "love", "you"]
encoded = solution.encode(strs)
print("Encoded:", encoded)  # Expected: "4#neet4#code4#love3#you"
decoded = solution.decode(encoded)
print("Decoded:", decoded)  # Expected: ["neet", "code", "love", "you"]


