class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        spiral_matrix = []
        row = col = up = left = right = down = 0
        num_elements = len(matrix) * len(matrix[0])

        while len(spiral_matrix) < num_elements:
            up += 1
            while col < len(matrix[0]) - right and len(spiral_matrix) < num_elements:
                spiral_matrix.append(matrix[row][col])
                col += 1
            col -= 1
            row += 1

            right += 1
            while row < len(matrix) - down and len(spiral_matrix) < num_elements:
                spiral_matrix.append(matrix[row][col])
                row += 1
            row -= 1
            col -= 1

            down += 1
            while col >= left and len(spiral_matrix) < num_elements:
                spiral_matrix.append(matrix[row][col])
                col -= 1
            col += 1
            row -= 1

            left += 1
            while row > up and len(spiral_matrix) < num_elements:
                spiral_matrix.append(matrix[row][col])
                row -= 1

        return spiral_matrix
