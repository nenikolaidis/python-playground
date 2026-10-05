# Given board
EXAMPLE_BOARD = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 0, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

count = 0
#Number Validation on row, col and block
def is_valid(board, row, col, num): 
    #Checking row
    for i in range(9):
        if board[row][i] == num:
            return False
    #Checking column
    for i in range(9):
        if board[i][col] == num:
            return False
    #Checking block 3x3
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
            
    return True

#Finding the best empty cell to start
def find_empty_cell(board):
    min_options = 10  
    best_cell = None

    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                options = 0
                #Checking options available
                for num in range(1, 10):
                    if is_valid(board, i, j, num):
                        options += 1
                if options < min_options:
                    min_options = options
                    best_cell = (i, j)
                    #If there is a cell with mininum options = 1 we stop the search and go for input
                    if min_options == 1:
                        return best_cell  
    return best_cell

#Function for solving the board
def solve_sudoku(board):
    global count
    empty_cell = find_empty_cell(board)
    if not empty_cell:
        return True

    row, col = empty_cell
    
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num

            if solve_sudoku(board):
                return True #Sudoku board is solved
            
            board[row][col] = 0  # Undo the move
            count += 1
    
    return False

def main():
    board = [row[:] for row in EXAMPLE_BOARD]
    if solve_sudoku(board):
        print("Solved Board:")
        for row in board:
            print(row)
    else:
        print("No solution exists.")

    print("Backtracking steps:", count)


if __name__ == "__main__":
    main()
