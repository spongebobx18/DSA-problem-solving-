def calculate_max(board_row, board_col, board):
    max_sum = 0
    for r in range(0, board_row):
        for c in range(0, board_col):
            n_sum = board[r][c]
            row, col = r, c
            
            # Upper left
            while row > 0 and col > 0:
                row -= 1
                col -= 1
                n_sum += board[row][col]
                
            row, col = r, c
            # Upper right
            while row > 0 and col < board_col - 1:
                row -= 1
                col += 1
                n_sum += board[row][col]
                
            row, col = r, c
            # Lower left
            while row < board_row - 1 and col > 0:
                row += 1
                col -= 1
                n_sum += board[row][col]
                
            row, col = r, c
            # Lower right
            while row < board_row - 1 and col < board_col - 1:
                row += 1
                col += 1
                n_sum += board[row][col]
            
            max_sum = max(max_sum, n_sum)
    
    return max_sum


N = int(input())

for _ in range(0, N):
    dimension = list(map(int, input().split()))
    board_row = dimension[0]
    board_col = dimension[1]
    board = [list(map(int, input().split())) for _ in range(0, board_row)]
    
    max_sum = calculate_max(board_row, board_col, board)
            
    print(max_sum)
