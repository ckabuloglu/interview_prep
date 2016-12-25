'''
Determine if a Sudoku is valid

https://leetcode.com/problems/valid-sudoku/
'''

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        nums = "123456789"
        
        # check for rows
        for row in board:
            container = {n: 0 for n in range(9)}
            for cell in row:
                if cell in nums:
                    if container[int(cell) - 1] > 0:
                        return False
                    else:
                        container[int(cell) - 1] = 1
                        
        # check for columns
        for cell in range(9):
            container = {n: 0 for n in range(9)}
            for col in range(9):
                num = board[col][cell]
                if num in nums:
                    if container[int(num) - 1] > 0:
                        return False
                    else:
                        container[int(num) - 1] = 1
        
        # check for subsquares
        starts = [1,4,7]
        for i in starts:
            for j in starts:
                container = {n: 0 for n in range(9)}
                for row in range(i, i+3):
                    for col in range(j, j+3):
                        num = board[row-1][col-1]
                        if num in nums:
                            if container[int(num) - 1] > 0:
                                return False
                            else:
                                container[int(num) - 1] = 1
      
        return True