"""
File: tic_tac_toe.py
---------------
Insert comment...
Jacopo Mascitelli
"""


def commit_move(board, sign, pos):
    board[pos] = sign


def check_free(board, pos):
    return board[pos] == " "


def winner(board, sign):
    return (board[7])


def make_board():
    board = []
    for y in range(3):
        row = []
        for x in range(3):
            row.append(" ")
        board.append(row)
    return board


def display_board(board):
    print("")
    for i in range(len(board)):
        print("    " + " | " + "   " + " | ")
        for z in range(len(board[i])):
            if z < (len(board[i]) - 1):
                print("  " + str(board[i][z]) + "  " + "|", end="")
            else:
                print("  " + str(board[i][z]) + "  ")
        if i < (len(board) - 1):
            print("    " + " | " + "   ", end="")
            print(" | ")
            print("-----------------")
    print("    " + " | " + "   " + " | ")
    print("")


def full_board(board):
    if " " in board:
        return True
    return False


def move_player(board):
    while True:
        pos = input("Place X in positions from 1 to 9")
        try:
            pos = int(pos)
            if 0 < pos < 10:
                if check_free(board, pos):
                    commit_move(board, "X", pos)
                    break
            else:
                print("Please insert a valid input.")
        except:
            print("Please insert a valid input.")

def move_comp():
    

def main():
    board = make_board()
    display_board(board)

    while not full_board(board):
        if winner(board, "O"):
            print("Computer Wins!")
            break
        if winner(board, "X"):
            print("Player Wins!")
            break
        else:
            move_player(board)
            move_comp()
            display_board(board)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
