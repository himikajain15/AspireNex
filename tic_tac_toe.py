import numpy as np

# Define the board
board = np.full((3, 3), ' ')

# Print the board
def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

# Check if a move is valid
def is_valid_move(board, row, col):
    return board[row][col] == ' '

# Make a move
def make_move(board, row, col, player):
    if is_valid_move(board, row, col):
        board[row][col] = player
        return True
    return False

# Check for win
def check_win(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all([board[i][j] == player for j in range(3)]) or all([board[j][i] == player for j in range(3)]):
            return True
    if board[0][0] == board[1][1] == board[2][2] == player or board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

# Check for draw
def check_draw(board):
    return all([board[i][j] != ' ' for i in range(3) for j in range(3)])

# Switch player
def switch_player(player):
    return 'O' if player == 'X' else 'X'

def minimax(board, depth, is_maximizing, alpha, beta):
    if check_win(board, 'O'):
        return 1
    if check_win(board, 'X'):
        return -1
    if check_draw(board):
        return 0

    if is_maximizing:
        best_score = -np.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    score = minimax(board, depth + 1, False, alpha, beta)
                    board[i][j] = ' '
                    best_score = max(score, best_score)
                    alpha = max(alpha, score)
                    if beta <= alpha:
                        break
        return best_score
    else:
        best_score = np.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    score = minimax(board, depth + 1, True, alpha, beta)
                    board[i][j] = ' '
                    best_score = min(score, best_score)
                    beta = min(beta, score)
                    if beta <= alpha:
                        break
        return best_score

def best_move(board):
    best_score = -np.inf
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                score = minimax(board, 0, False, -np.inf, np.inf)
                board[i][j] = ' '
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

def play_game():
    current_player = 'X'
    while True:
        print_board(board)
        if current_player == 'X':
            row, col = map(int, input("Enter your move (row and column): ").split())
            if not make_move(board, row, col, current_player):
                print("Invalid move. Try again.")
                continue
        else:
            move = best_move(board)
            if move:
                make_move(board, move[0], move[1], current_player)
        
        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        current_player = switch_player(current_player)

play_game()
