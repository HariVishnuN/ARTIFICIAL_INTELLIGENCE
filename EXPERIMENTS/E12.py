def print_board(b):
    for i in range(0, 9, 3): print(f"{b[i]} | {b[i+1]} | {b[i+2]}")
def check_win(b, p):
    w = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    return any(b[i] == b[j] == b[k] == p for i, j, k in w)
if __name__ == "__main__":
    board = [' '] * 9
    player = 'X'
    for _ in range(9):
        print_board(board)
        pos = int(input(f"Player {player}, enter position (1-9): ")) - 1
        if board[pos] == ' ':
            board[pos] = player
            if check_win(board, player):
                print_board(board)
                print(f"Player {player} wins!")
                break
            player = 'O' if player == 'X' else 'X'
        else:
            print("Position taken. You lose your turn.")
    else:
        print_board(board)
        print("Draw!")