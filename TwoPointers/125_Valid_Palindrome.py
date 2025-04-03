'''
125. Valid Palindrome
Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
'''

# Brute Force
# Time Complexity: O(n)
# Space Complexity: O(n)

'''
Below is the code for the brute force approach.
It uses the built-in string methods to clean the input string and check if it is a palindrome.
'''

class Solution:
    def isPalindrome(self, s):
        clean = ''.join(c for c in s if c.isalnum()).lower()
        return clean == clean[::-1]
    
# Two Pointers
# Time Complexity: O(n)
# Space Complexity: O(n)

'''
Below is the code for the two pointers approach.
It uses two pointers to check if the cleaned string is a palindrome.
The two pointers start at the beginning and end of the string and move towards the center, comparing characters along the way.
If any characters don't match, it returns False. If all characters match, it returns True.
'''

class Solution:
    def isPalindrome(self, s):
        clean = ''.join(c for c in s if c.isalnum()).lower()
        i=0 
        j=len(clean)-1
        
        while i<=j:
            if clean[i]!=clean[j]:
                return False
            else:
                i+=1
                j-=1
        return True
    
# Two Pointers (Optimized)
# Time Complexity: O(n)
# Space Complexity: O(1)

'''
This approach uses the two-pointer technique to efficiently check if a string is a palindrome 
while ignoring non-alphanumeric characters and treating uppercase and lowercase letters as the same
'''

class Solution:
    def isPalindrome(self, s):
        i=0
        j=len(s)-1
        
        while i<j:
            while i<j and not s[i].isalnum():
                i+=1
            while i<j and not s[j].isalnum():
                j-=1
            
            if s[i].lower()!=s[j].lower():
                return False
            
            i+=1
            j-=1
        return True
    
sol = Solution()
s = "Was it a car or a cat I saw?"
print(sol.isPalindrome(s))
# Output: True
