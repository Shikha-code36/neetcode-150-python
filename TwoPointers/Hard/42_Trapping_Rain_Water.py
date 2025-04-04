'''
42. Trapping Rain Water

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9
Explanation: The above elevation map (black section) is represented by array [4,2,0,3,2,5]. In this case, 9 units of rain water (blue section) are being trapped.
'''

# Brute Force
# Time Complexity: O(n^2)
# Space Complexity: O(1)

'''
Brute Force Approach:

We iterate through each element in the height array and calculate the amount of water that can be trapped above it.
For each element at index `i`, we:
1. Find the **maximum height to the left** (including `height[i]`) → `left_max = max(height[:i+1])`
2. Find the **maximum height to the right** (including `height[i]`) → `right_max = max(height[i:])`
3. The trapped water at `i` is given by:
      trapped_water[i] = min(left_max, right_max) - height[i]

Since for each `i`, we traverse the left and right side separately, the time complexity is **O(n²)**.
The space complexity is **O(1)** as we don't use extra data structures.
'''


class Solution:
    def trap(self, height):
        n=len(height)
        
        total_water =0
        
        for i in range(n):
            left_max = max(height[:i+1])
            right_max = max(height[i:])
            total_water+= min(left_max,right_max)-height[i]
            
        return total_water  
    
# Left and Right Max Array
# Time Complexity: O(n)
# Space Complexity: O(n)

'''
Optimized Approach: Left and Right Max Arrays (O(n) Time, O(n) Space)

To optimize the brute force approach, we precompute the maximum height to the left and right for each element.

1. We create two arrays:
   - `left_max[i]`: Stores the maximum height **from index 0 to i** (including `i`).
   - `right_max[i]`: Stores the maximum height **from index n-1 to i** (including `i`).

2. We compute `left_max[]`:
   - Traverse from `left to right`, storing the highest wall encountered so far.

3. We compute `right_max[]`:
   - Traverse from `right to left`, storing the highest wall encountered so far.

4. Finally, we iterate through the array to calculate trapped water:
   - `trapped_water[i] = min(left_max[i], right_max[i]) - height[i]`

**Time Complexity:** O(n) (We traverse the array three times: once to compute `left_max[]`, once for `right_max[]`, and once to calculate trapped water).  
**Space Complexity:** O(n) (We store two extra arrays `left_max[]` and `right_max[]`).
'''


class Solution:
    def trap(self, height):
        n=len(height)
        
        total_water =0
        left_max=[0]*n
        right_max=[0]*n
        
        left_max[0]=height[0]
        for i in range(1,n):
            left_max[i] = max(left_max[i-1],height[i])
        
        right_max[n-1]=height[n-1]
        for i in range(n-2,-1,-1):
            right_max[i] = max(right_max[i+1], height[i])
        
        for i in range(n):
            total_water+= min(left_max[i],right_max[i])-height[i]
            
        return total_water
    

# Two Pointers Approach
# Time Complexity: O(n)
# Space Complexity: O(1)

'''
In this approach, we use two pointers to traverse the height array from both ends towards the center.
1. Initialize two pointers: `left` at the start (0) and `right` at the end (n-1) of the array.
2. Initialize two variables `left_max` and `right_max` to keep track of the maximum heights encountered so far from both ends.
3. While `left` is less than or equal to `right`:

    - If `height[left]` is less than or equal to `height[right]`:
        - If `height[left]` is greater than or equal to `left_max`, update `left_max`.
        - Otherwise, calculate the trapped water at `left` using `left_max` and add it to the total water.
        - Move the `left` pointer one step to the right.
    - Else:
        - If `height[right]` is greater than or equal to `right_max`, update `right_max`.
        - Otherwise, calculate the trapped water at `right` using `right_max` and add it to the total water.
        - Move the `right` pointer one step to the left.
4. Continue this process until the two pointers meet.
5. Return the total water trapped.
'''

class Solution:
    def trap(self, height):
        n=len(height)
        
        total_water =0
        left_max=0
        right_max=0
        
        l=0
        r=n-1
        
        while l<r:
            if height[l]<height[r]:
                if height[l]>=left_max:
                    left_max=height[l]
                else:
                    total_water+=left_max-height[l]
                l+=1
            else:
                if height[r]>=right_max:
                    right_max=height[r]
                else:
                    total_water+=right_max-height[r]
                r-=1
        return total_water
                
    
    
sol = Solution()
heights = [0,1,0,2,1,0,1,3,2,1,2,1]
print(sol.trap(heights))  # Output: 6