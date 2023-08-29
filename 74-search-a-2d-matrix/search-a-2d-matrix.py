# class Solution:
#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#         row, col = 0, len(matrix[0])-1
#         while row < len(matrix) and col >= 0 :
#             if matrix[row][col] == target :
#                 return True
#             elif matrix[row][col] >= target :
#                 col -= 1
#             else :
#                 row += 1
#         return False

# this was our solution, although it needs a little work. 

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        
        row_length = len(matrix)
        col_length = len(matrix[0])
        row = 0
        col = col_length - 1
        
        while col >= 0 and row < row_length:
            if target == matrix[row][col]:
                return True
            elif target < matrix[row][col]:
                col -= 1
            else:
                row += 1
        
        return False