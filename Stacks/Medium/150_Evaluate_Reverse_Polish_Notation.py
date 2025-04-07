'''
150. Evaluate Reverse Polish Notation

You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:

The valid operators are '+', '-', '*', and '/'.
Each operand may be an integer or another expression.
The division between two integers always truncates toward zero.
There will not be any division by zero.
The input represents a valid arithmetic expression in a reverse polish notation.
The answer and all the intermediate calculations can be represented in a 32-bit integer.
 

Example 1:

Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
Example 2:

Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
Example 3:

Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
 

Constraints:

1 <= tokens.length <= 104
tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200].
'''

# Brute Force (without stack)
# Time Complexity: O(n^2)
# Space Complexity: O(n)

'''
In this approach, we are going to iterate through the tokens and check if the token is an operator or not.
if token is an operand then our op will be that toekn[i].

A will token[i-2] and B will be token[i-1].
Then we will check the operator and perform the operation.
We will  mutate the tokens list and remove the operands and operator from the list.
We will store the result in the tokens list and update the pointer to 0 else we will increment the pointer by 1.
We will repeat this process until we have only one element in the tokens list.

Then we will return the first element of the tokens list.
We will convert the result to int and return it.
'''

class Solution:
    def evalRPN(self, tokens):
        res = None
        
        i=0
        while len(tokens)>1:
            if tokens[i] in "*+-/":
                op = tokens[i]
                a = int(tokens[i - 2])
                b = int(tokens[i - 1])
                

                if op == "*":
                    res = a*b
                elif op == "-":
                    res = a-b
                elif op == "+":
                    res = a+b
                elif op == "/":
                    res = int(a/b)
                    
                tokens = tokens[:i - 2] + [str(res)] + tokens[i + 1:]
                i=0
            else:
                i+=1
                
        return int(tokens[0])
    
# Optimal Approach (using stack)
# Time Complexity: O(n)
# Space Complexity: O(n)

'''
In this approach we are going to use stack to solve the problem.
We will iterate through the tokens and check if the token is an operator or not.
If it is an operand then we will append it to the stack after converting it to int.
If it is an operator then we will pop the last two elements from the stack and perform the operation.
We will append the result to the stack.
We will repeat this process until we have only one element in the stack.
Then we will return the first element of the stack.
'''

class Solution:
    def evalRPN(self, tokens):
        stack=[]
        res =  None
        
        for i in range(len(tokens)):
            if tokens[i] not in "+-*/":
                stack.append(int(tokens[i]))
            
            else:
                a= stack.pop()
                b= stack.pop()
                if tokens[i] == "+":
                    res = b + a
                elif tokens[i] == "-":
                    res = b - a
                elif tokens[i] == "*":
                    res = b * a
                elif tokens[i] == "/":
                    res = int(b/a)
                stack.append(res)
        return stack[0]
            
    
obj = Solution()
tokens=["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(obj.evalRPN(tokens)) # Output: 22