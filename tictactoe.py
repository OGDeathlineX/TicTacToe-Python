import time
import random
import os

#Player Selection
letter = ''
cpu_letter = ''

#Depth
depth=0

def playerSelection():
    print("Select your character X or O:")
    letter = input()
    while not (letter == 'X' or letter == 'O' or letter == 'x' or letter == 'o'):
        letter = input()
    if letter == 'x':
        letter = 'X'
    if letter == 'o':
        letter = 'O'

    if letter == 'X':
        cpu_letter = 'O'
    else:
        cpu_letter = 'X'
    print('Player = ' + letter + ' | CPU = ' + cpu_letter + "\n")
    setDifficulty(letter, cpu_letter)

#Board
def ConstBoardX(board, letter, cpu_letter):
    print("Current State Of Board : \n\n");
    for i in range (0,9):
        if((i>0) and (i%3)==0):
            print("\n");
        if(board[i]==0):
            print("- ",end=" ");
        if (board[i]==1):
            print(cpu_letter + " ",end=" ");
        if(board[i]==-1):    
            print(letter + " ",end=" ");
    print("\n\n");


#Main Page
def mainPage():
    print('TIC TAC TOE MINIMAX PROJECT')
    print('     ||     ||')
    print('  X  ||     ||  X')
    print('     ||     ||')
    print('---------------------')
    print('     ||     ||')
    print('     ||  O  ||')
    print('     ||     ||')
    print('---------------------')
    print('     ||     ||')
    print('     ||     ||  O')
    print('     ||     ||')

#Difficulty
def minimax(board,player,depth):
    x=analyzeboard(board);
    if(x!=0):
        return (x*player);
    pos=-1;
    value=-2;
    for i in range(0,9):
        if(board[i]==0):
            board[i]=player;
            score=-minimax(board,(player*-1));
            if(score>value):
                value=score;
                pos=i;
            board[i]=0;
    if(pos==-1):
        return 0;
    return value;

def User1Turn(board):
    pos=input("Enter " + letter + "'s position from [1...9]: ");
    pos=int(pos);
    if(board[pos-1]!=0):
        print("Select a valid position");
        exit(0) ;
    board[pos-1]=-1;

def CompTurn(board,difficulty):
    if difficulty == 1:
        depth=3
        depth = int(depth)
    if difficulty == 2:
        depth=5
        depth = int(depth)
    if difficulty == 3:
        depth=9
        depth = int(depth)
    pos=-1;
    value=-2;
    for i in range(0,9):
        if(board[i]==0):
            board[i]=1;
            score=-minimax(board, -1, depth);
            board[i]=0;
            if(score>value):
                value=score;
                pos=i;
    board[pos]=1;

def analyzeboard(board):
    cb=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]];

    for i in range(0,8):
        if(board[cb[i][0]] != 0 and
           board[cb[i][0]] == board[cb[i][1]] and
           board[cb[i][0]] == board[cb[i][2]]):
            return board[cb[i][2]];
    return 0;

def setDifficulty(letter, cpu_letter):
    print('Select your difficulty: \n' + "1. Easy (3 levels of decisions tree) \n" + "2. Normal (5 levels of decisions tree) \n" + "3. HARDCORE (All tree)")
    difficulty = input()
    #In terms to make easier the logic and heuristic, we decided to program the tic tac toe's board in 1 array.
    #In the minimax algorithm player moves 1 and cpu move -1.
    board=[0,0,0,0,0,0,0,0,0];
    player= input("Before start: Enter to play 1(st) or 2(nd) :");
    player = int(player);
 
    for i in range (0,9):
        if(analyzeboard(board)!=0):
            break;
        if((i+player)%2==0):
            CompTurn(board,difficulty);
        else:
            ConstBoardX(board, letter, cpu_letter);
            User1Turn(board);
    else:
        for i in range (0,9):
            if(analyzeboard(board)!=0):
                break;
            if((i)%2==0):
                ConstBoardX(board, letter, cpu_letter);
                User1Turn(board);
    x=analyzeboard(board);
 
    if(x==-1):
         ConstBoardX(board, letter, cpu_letter);
         print("PLAYER WINS!")
    if(x==1):
         ConstBoardX(board, letter, cpu_letter);
         print("IA WINS!")
    else:
         ConstBoardX(board, letter, cpu_letter);
         print("IT'S A DRAW!")

#Execution
mainPage()
playerSelection()
