'''
155. Min Stack

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
Implement a min stack that supports the following operations:

- `push(val)`: Pushes the element val onto the stack.
- `pop()`: Removes the element on the top of the stack.
- `top()`: Gets the top element of the stack.
- `getMin()`: Retrieves the minimum element in the stack.

You must implement a solution with O(1) time complexity for each function.

Example 1:
Input
["MinStack", "push", "push", "push", "getMin", "pop", "top", "getMin"]
[[], [-2], [0], [-3], [], [], [], []]
Output
[null, null, null, null, -3, null, 0, -2]
Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   // return -3
minStack.pop();
'''

# Brute Force Approach
# Time Complexity: O(n) for getMin() operation
# Space Complexity: O(n) for storing elements in stack

'''
In this brute force approach, we use a single stack to store all the values.
The `push`, `pop`, and `top` operations work in O(1) time.

However, the `getMin()` operation uses Python’s built-in `min()` function,
which scans the entire stack to find the minimum value, resulting in O(n) time complexity.

This approach works fine for small inputs but becomes inefficient when the number of elements is large.
'''

class MinStack:

    def __init__(self):
        self.stack = []       

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return min(self.stack)
    

# Optimized Approach
# Time Complexity: O(1) for all operations
# Space Complexity: O(n) for storing elements in stack and min_stack

'''
In this optimized approach, we use two stacks:
1. `stack` - to store all the values.
2. `min_stack` - to keep track of the current minimum value at every point in time.

When pushing a value, we also push it to `min_stack` if it is smaller than or equal to the current minimum.
When popping a value, if it is the same as the current minimum (top of `min_stack`), we also pop from `min_stack`.

This ensures that `getMin()` always returns the top of `min_stack` in O(1) time.
All operations—`push`, `pop`, `top`, and `getMin()`—run in constant time.
This approach is more efficient and suitable for large inputs.
'''

class MinStack:

    def __init__(self):
        self.stack = []   
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        if self.stack:
            popped = self.stack.pop()
            if popped == self.min_stack[-1]:
                self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
    

minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
minStack.getMin()
minStack.pop()
print(minStack.top())
print(minStack.getMin())

     