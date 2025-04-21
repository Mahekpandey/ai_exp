import math

# Constants for players
PLAYER = 'X'
OPPONENT = 'O'
EMPTY = ' '

# Function to check if any moves are left
def is_moves_left(board):
    return any(cell == EMPTY for row in board for cell in row)

# Evaluation function
def evaluate(board):
    # Rows
    for row in board:
        if row[0] == row[1] == row[2] != EMPTY:
            return 10 if row[0] == PLAYER else -10

    # Columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != EMPTY:
            return 10 if board[0][col] == PLAYER else -10

    # Diagonals
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return 10 if board[0][0] == PLAYER else -10
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return 10 if board[0][2] == PLAYER else -10

    return 0

# Minimax function
def minimax(board, depth, is_max):
    score = evaluate(board)

    if score == 10 or score == -10:
        return score

    if not is_moves_left(board):
        return 0

    if is_max:
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER
                    best = max(best, minimax(board, depth + 1, False))
                    board[i][j] = EMPTY
        return best
    else:
        best = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = OPPONENT
                    best = min(best, minimax(board, depth + 1, True))
                    board[i][j] = EMPTY
        return best

# Function to find the best move
def find_best_move(board):
    best_val = -math.inf
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                board[i][j] = PLAYER
                move_val = minimax(board, 0, False)
                board[i][j] = EMPTY

                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val

    return best_move

# Example board
board = [
    [PLAYER, OPPONENT, PLAYER],
    [OPPONENT, PLAYER, EMPTY],
    [EMPTY, EMPTY, OPPONENT]
]

best_move = find_best_move(board)
print("The best move is at row:", best_move[0], "col:", best_move[1])
