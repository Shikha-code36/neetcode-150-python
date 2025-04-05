'''
20. Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.
Note that an empty string is also considered valid.

Example 1:
Input: s = "()"
Output: true
Example 2:
Input: s = "()[]{}"
Output: true
Example 3:
Input: s = "(]"
Output: false
'''
# Brute Force Approach
# Time Complexity: O(n^2)
# Space Complexity: O(n)

'''
In the brute force approach, we can use a while loop to check if there are any pairs of brackets that can be removed from the string.
We can keep removing pairs of brackets until no more pairs can be removed. 
If the string becomes empty, it means all brackets were matched and we return True. If there are still brackets left in the string, we return False.
'''

class Solution:
    def isValid(self, s):
        while "()" in s or "[]" in s or "{}" in s:
            s = s.replace("()", "")
            s = s.replace("[]", "")
            s = s.replace("{}", "")
            
        return s == ""

# Stack Approach
# Time Complexity: O(n), where n is the length of the string.
# Space Complexity: O(n), in the worst case, we need to store all opening brackets in the stack.

'''
Below is the code to solve the problem:
1. Create a stack to keep track of the opening brackets.
2. Create a mapping of opening brackets to closing brackets.
3. Iterate through each character in the string:
    - If the character is an opening bracket, push it onto the stack.
    - If the character is a closing bracket, check if the stack is empty or if the top of the stack does not match the corresponding opening bracket. 
            If either condition is true, return False.
    - If the character is a closing bracket and the stack is not empty, pop the top of the stack.
4. After iterating through the string, check if the stack is empty. If it is, return True; otherwise, return False.
'''
class Solution:
    def isValid(self, s):
        stack = []
        mapp = {"(":")","[":"]","{":"}"}
        for ch in s:
            if ch in mapp:
                stack.append(ch)
            elif ch in mapp.values():
                if not stack or mapp[stack.pop()]!=ch:
                    return False
        return True if not stack else False
                    

class Solution:
    def isValid(self, s):
        stack = []
        mapp = { ")" : "(", "]" : "[", "}" : "{" }

        for c in s:
            if c in mapp:
                if stack and stack[-1] == mapp[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False
    
obj = Solution()
s = "([{}])"
print(obj.isValid(s)) # Output: True