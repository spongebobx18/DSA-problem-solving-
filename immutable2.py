class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        

    
        if not matrix:
            return

        rows = len(matrix)
        cols = len(matrix[0])
        for i in range(1, rows):
            matrix[i][0] += matrix[i-1][0]
        for j in range(1, cols):
            matrix[0][j] += matrix[0][j-1]

        
        for i in range(1, rows):
            for j in range(1, cols):
                matrix[i][j] += matrix[i - 1][j] + matrix[i][j - 1] - matrix[i - 1][j - 1]
        
        self.matrix=matrix
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        topleft=self.matrix[row1-1][col1-1] 
        up=self.matrix[row1-1][col2]
        left_matrix=self.matrix[row2][col1-1]
        NumMatrix= self.matrix[row2][col2]-up-left_matrix+topleft
        return NumMatrix


        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)