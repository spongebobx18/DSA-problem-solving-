class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):#to be able to search the first index array
                if [row][col]==target:
                    return True 
        return False        