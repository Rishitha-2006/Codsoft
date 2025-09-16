import math

# Initialize board
board = [" " for _ in range(9)]

def print_board():
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print("|".join(row))
    print()

def available_moves():
    return [i for i, spot in enumerate(board) if spot == " "]

def winner(b, player):
    win_states = [
        [0,1,2], [3,4,5], [6,7,8], # rows
        [0,3,6], [1,4,7], [2,5,8], # cols
        [0,4,8], [2,4,6]           # diagonals
    ]
    return any(all(b[i] == player for i in combo) for combo in win_states)

def minimax(b, depth, is_maximizing):
    if winner(b, "O"):  # AI wins
        return 1
    elif winner(b, "X"):  # Human wins
        return -1
    elif " " not in b:  # Draw
        return 0

    if is_maximizing:
        best_score = -math.inf
        for move in available_moves():
            b[move] = "O"
            score = minimax(b, depth + 1, False)
            b[move] = " "
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for move in available_moves():
            b[move] = "X"
            score = minimax(b, depth + 1, True)
            b[move] = " "
            best_score = min(score, best_score)
        return best_score

def best_move():
    best_score = -math.inf
    move = None
    for i in available_moves():
        board[i] = "O"
        score = minimax(board, 0, False)
        board[i] = " "
        if score > best_score:
            best_score = score
            move = i
    return move

# Game loop
def play():
    print("Tic Tac Toe! You are X, AI is O")
    print_board()

    while True:
        # Human move
        human_move = int(input("Enter your move (0-8): "))
        if board[human_move] != " ":
            print("Invalid move! Try again.")
            continue
        board[human_move] = "X"

        if winner(board, "X"):
            print_board()
            print("You win!")
            break
        elif " " not in board:
            print_board()
            print("It's a draw!")
            break

        # AI move
        ai_move = best_move()
        board[ai_move] = "O"
        print("AI chooses position", ai_move)

        print_board()

        if winner(board, "O"):
            print("AI wins!")
            break
        elif " " not in board:
            print("It's a draw!")
            break

play()