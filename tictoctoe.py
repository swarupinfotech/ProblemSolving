board = [' ' for _ in range(9)]

def print_board():
    for i in range(0, 9, 3):
        print(board[i], '|', board[i+1], '|', board[i+2])

def check_winner(player):
    win_conditions = [
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

for turn in range(9):
    print_board()
    player = 'X' if turn % 2 == 0 else 'O'
    move = int(input(f"Player {player}, enter position (0-8): "))
    board[move] = player

    if check_winner(player):
        print_board()
        print(f"Player {player} wins!")
        break
else:
    print("Draw!")
