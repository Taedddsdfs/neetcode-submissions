class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROW,COL = len(matrix),len(matrix[0])
        l,r = 0, ROW-1
        while l<=r:
            m = (l+r)//2
            if target>matrix[m][-1]:
                l = m+1
            elif target<matrix[m][0]:
                r = m-1
            else:
                break
        if not (l<=r):
            return False
        
        row = (l+r)//2
        l,r = 0,COL-1
        while l<=r:
            m = (l+r)//2
            if target>matrix[row][m]:
                l = m+1
            elif target<matrix[row][m]:
                r= m-1
            else:
                return True
        return False

        