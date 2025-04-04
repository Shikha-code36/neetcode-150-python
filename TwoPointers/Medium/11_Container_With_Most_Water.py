'''
11. Container With Most Water

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the line i is at (i, 0) and (i, height[i]). Find two lines, which together with the x-axis form a container, such that the container contains the most water.
You may not slant the container and n is at least 2.
Return the maximum amount of water a container can store.
The answer is guaranteed to be less than or equal to 10^4.

Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water the container can contain is 49.

Example 2:
Input: height = [1,1]
Output: 1
Explanation: The above vertical lines are represented by array [1,1]. In this case, the max area of water the container can contain is 1.
'''

#Note:
'''
- The container can only hold water if the two lines are not the same.
- The area of water that can be contained between two lines is determined by the shorter line and the distance between the two lines.
- The maximum area is the maximum of all possible areas that can be formed by any two lines.

Why we chose j-i as width?
- The width of the container is determined by the distance between the two lines.

Why we chose min(height[i], height[j]) as height?
- The height of the container is determined by the shorter of the two lines, as water cannot overflow the shorter line.

- The area of the container is then calculated as width * height, which is (j - i) * min(height[i], height[j]).
'''


# Brute Force
# Time Complexity: O(n^2)
# Space Complexity: O(1)

'''
So in the brute force approach, we will iterate through all the pairs of lines and calculate the area of water that can be contained between them. 
The area is calculated as min(height[i], height[j]) * (j - i), where i and j are the indices of the two lines. 
We will keep track of the maximum area found so far and return it at the end.
'''

class Solution:
    def maxArea(self, height):
        max_area=0
        
        for i in range(len(height)):
            for j in range(i+1, len(height)):
                new_h=min(height[i],height[j])
                width = j-i
                area= new_h*width
                max_area=max(area,max_area)
                
        return max_area
    
# Two Pointers
# Time Complexity: O(n)
# Space Complexity: O(1)

'''
The two pointers approach is a more efficient way to solve the problem.
In this approach, we start with two pointers, one at the beginning of the array and one at the end.
We calculate the area of water that can be contained between the two lines at the pointers and update the maximum area found so far. 
Then we move the pointer pointing to the shorter line towards the other pointer. I mean if left wall is shorter than right wall, we move left pointer to the right.
If the right wall is shorter, we move the right pointer to the left.
This is because the area is limited by the shorter line, so moving the pointer pointing to the shorter line may lead to a larger area.
We repeat this process until the two pointers meet.
'''
class Solution:
    def maxArea(self, heights):
        max_area=0
        
        l=0
        r=len(heights)-1
        
        while l<r:
            height=min(heights[l],heights[r])
            width=r-l
            area=height*width
            max_area=max(area,max_area)
            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1
                
        return max_area
        
    
    
sol = Solution()
heights = [1,8,6,2,5,4,8,3,7]
print(sol.maxArea(heights))