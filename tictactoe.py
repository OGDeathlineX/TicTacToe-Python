import time
import random
import os

# Player Selection
letter = ""
cpu_letter = ""
cont = 0

def playerSelection():
    print("Select your character X or O:")
    letter = input()
    while not (letter == "X" or letter == "O" or letter == "x" or letter == "o"):
        letter = input()
    if letter == "x":
        letter = "X"
    if letter == "o":
        letter = "O"

    if letter == "X":
        cpu_letter = "O"
    else:
        cpu_letter = "X"
    print("Player = " + letter + " | CPU = " + cpu_letter + "\n")
    setDifficulty(letter, cpu_letter)

# Board
# Print the next board
#
#   -   -   -
#
#   -   -   -
#
#   -   -   -

def ConstBoardX(board, letter, cpu_letter):
    print("Current State Of Board : \n\n")
    for i in range(0, 9):
        if (i > 0) and (i % 3) == 0:
            print("\n")
        if board[i] == 0:
            print("- ", end=" ")
        if board[i] == 1:
            print(cpu_letter + " ", end=" ")
        if board[i] == -1:
            print(letter + " ", end=" ")
    print("\n\n")

# Main Page
def mainPage():
    print("TIC TAC TOE MINIMAX PROJECT")
    print("     ||     ||")
    print("  X  ||     ||  X")
    print("     ||     ||")
    print("---------------------")
    print("     ||     ||")
    print("     ||  O  ||")
    print("     ||     ||")
    print("---------------------")
    print("     ||     ||")
    print("     ||     ||  O")
    print("     ||     ||")

# Difficulty
# User's turn
def UserTurn(board):
    pos = input("Enter " + letter + "'s position from [1 - 9]: ")
    pos = int(pos)
    if board[pos - 1] != 0:
        print("Select a valid position")
        exit(0)
    board[pos - 1] = -1

# IA's turn
def IaTurn(board, difficulty):
    pos = -1
    value = -2
    for i in range(0, 9):
        if board[i] == 0:
            board[i] = 1
            score = -minimax(board, -1, difficulty)
            board[i] = 0
            if score > value:
                value = score
                pos = i
    board[pos] = 1

# Minimax algorithm
def minimax(board, player, difficulty):
    game = analyzeboard(board)
    if game != 0:
        return game * player
    pos = -1
    value = -2
    cont = 0
    for i in range(0, 9):
        if board[i] == 0:
            board[i] = player
            score = -minimax(board, (player * -1), difficulty)
            cont = cont + 1
            if score > value:
                value = score
                pos = i
            board[i] = 0
        if difficulty == 1 and cont == 2:
            break
        if difficulty == 2 and cont == 4:
            break
    if pos == -1:
        return 0
    return value

def analyzeboard(board):
    # Cb it's equal to the victory cases, and this function analyze that the board meets with the  victory statements
    cb = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6],
    ]
    # Validation of the board, it returns the array and if its ocuppated by the player or the IA
    for i in range(0, 8):
        if (
            board[cb[i][0]] != 0
            and board[cb[i][0]] == board[cb[i][1]]
            and board[cb[i][0]] == board[cb[i][2]]
        ):
            return board[cb[i][2]]
    return 0


def setDifficulty(letter, cpu_letter):
    print(
        "Select your difficulty: \n"
        + "1. Easy (3 levels of decisions tree) \n"
        + "2. Normal (5 levels of decisions tree) \n"
        + "3. HARDCORE (All tree)"
    )
    difficulty = input()
    difficulty = int(difficulty)
    # In terms to make easier the logic and heuristic, we decided to program the tic tac toe's board in 1 array.
    # In the minimax algorithm player moves 1 and cpu move -1.
    board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    player = input("Before start: Enter to play 1(st) or 2(nd) :")
    player = int(player)

    for i in range(0, 9):
        if analyzeboard(board) != 0:
            break
        if (i + player) % 2 == 0:
            IaTurn(board, difficulty)
        else:
            ConstBoardX(board, letter, cpu_letter)
            UserTurn(board)

    # Once everyone done their respective move, game
    game = analyzeboard(board)
    game = int(game)
    if game == -1:
        ConstBoardX(board, letter, cpu_letter)
        print("PLAYER WINS!")
    elif game == 1:
        ConstBoardX(board, letter, cpu_letter)
        print("IA WINS!")
    elif game != 1 or game != -1:
        ConstBoardX(board, letter, cpu_letter)
        print("IT'S A DRAW!")

# Execution
mainPage()
playerSelection()
