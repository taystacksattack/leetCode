class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # run through the matrix once, and keep track of where the zeroes are
            # use a row set and column set
        # then run through it againn, and if see the row or column corresponds to a row or column we found a zero in, then we can set it to zero

        rows = set()
        cols = set()

        for r in range(len(matrix)):
            for c in range (len(matrix[0])):
                if matrix[r][c] == 0:
                    rows.add(r)
                    cols.add(c)
        
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if r in rows or c in cols:
                    matrix[r][c] = 0

#time = O(rc)
# space complexity O(r+c)
    #if you were making a copy of the array, it would be O(rc)