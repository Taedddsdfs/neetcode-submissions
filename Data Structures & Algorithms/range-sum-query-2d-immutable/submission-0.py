from typing import List

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            return
            
        ROWS, COLS = len(matrix), len(matrix[0])
        
        # Create a prefix sum matrix padded with an extra row and column of zeros
        # Size becomes (ROWS + 1) x (COLS + 1)
        self.pref = [[0] * (COLS + 1) for _ in range(ROWS + 1)]
        
        # Fill the prefix sum matrix
        for r in range(ROWS):
            for c in range(COLS):
                # Current pref = original val + top pref + left pref - diagonal pref
                self.pref[r + 1][c + 1] = (
                    matrix[r][c] 
                    + self.pref[r][c + 1] 
                    + self.pref[r + 1][c] 
                    - self.pref[r][c]
                )

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # Using the Inclusion-Exclusion Principle with shifted coordinates (+1)
        # Total rectangle - top rectangle - left rectangle + overlapping diagonal rectangle
        return (
            self.pref[row2 + 1][col2 + 1] 
            - self.pref[row1][col2 + 1] 
            - self.pref[row2 + 1][col1] 
            + self.pref[row1][col1]
        )

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)