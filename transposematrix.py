class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        
    
        rows = len(matrix)
        cols = len(matrix[0])
        transposed = [[0 for _ in range(rows)] for _ in range(cols)]# swapping sizes ensure that we get the correct shape in the transposed matrix everytime
        for i in range(rows):
            for j in range(cols):
                transposed[j][i] = matrix[i][j]

        return transposed
