'''
36. Valid Sudoku

Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
1. Each row must contain the digits 1-9 without repetition.
2. Each column must contain the digits 1-9 without repetition.
3. Each of the nine 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note:
A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.

Example 1:
Input: board = 
[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: true

Example 2:
Input: board = 
[
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: false
'''

# Approach:
# Time Complexity: O(N^2) where N is the number of cells in the board (81 cells).
# Space Complexity: O(N^2) for the sets used to track seen numbers in rows, columns, and boxes.
'''
We can use a set to keep track of the numbers we have seen in each row, column, and 3x3 sub-box.
We will iterate through each cell in the board and check if the number is already in the corresponding row, column, or sub-box set. 
If it is, we return false. If not, we add the number to the respective sets.
'''

class Solution:
    def isValidSudoku(self, board):
        row_count={}
        col_count={}
        box_count={}
        
        for r in range(9):
            for c in range(9):
                num = board[r][c]
                
                if num ==".":
                    continue
                bx_in= (r//3)*3+(c//3)
                if r not in row_count:
                    row_count[r]=set()
                if c not in col_count:
                    col_count[c]=set()
                if bx_in not in box_count:
                    box_count[bx_in]=set()
                
                if num in row_count[r] or num in col_count[c] or num in box_count[bx_in]:
                    return False
                
                row_count[r].add(num)
                col_count[c].add(num)
                box_count[bx_in].add(num)
                
        return True
                
                    

obj = Solution()
board =[["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]

print(obj.isValidSudoku(board))

        
