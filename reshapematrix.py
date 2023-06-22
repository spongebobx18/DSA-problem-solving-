import numpy as np

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])
        
        if rows * cols != r * c:
            return mat
        
        flattened_matrix = [num for row in mat for num in row]
        reshaped_matrix = np.reshape(flattened_matrix, (r, c))
        return reshaped_matrix.tolist()