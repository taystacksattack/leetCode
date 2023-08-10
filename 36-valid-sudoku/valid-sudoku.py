from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # use hash table to keep track of values in rows, columns, and boxes (the nine boxes of nine cells). 
        # essentially, when we go through and see if any values are repeated, then we can just return false.
        # use of // rounds down (like math.floor() in JS)

        row = defaultdict(set)
        col = defaultdict(set)
        box = defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board[0])):
                curr_val = board[r][c]

                if curr_val != '.':
                    box_coord = f'{r//3},{c//3}' #string interpolation, becomes key for box coordinate

                    if curr_val in row[r] or curr_val in col[c] or curr_val in box[box_coord]:
                        return False
                    row[r].add(curr_val)
                    col[c].add(curr_val)
                    box[box_coord].add(curr_val)
                
        return True