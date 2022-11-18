1import os
import time

board = [' ',' ',' ',' ', ' ', ' ',' ',' ',' ',' ']
player =1

##   WIN Flags   ##
Win =1
Draw = -1
Running = 0
stop = 1

#####################
Game = Running
Mark = 'X'

# This function Draws Game Board
def DrawBoard():
    print(" %c | %c | %c " % (board[1],board[2],board[3]))
    print("___|___|___")
    print(" %c | %c | %c " % (board[4],board[5],board[6]))
    print("___|___|___")
    print(" %c | %c | %c " % (board[7],board[8],board[9]))
    print("___|___|___")

# THis Function checks position is empty or not
def CheckPosition(x):
    if(board[x] == ' '):
        return True
    else:
        return False

# This Function Checks player has Won or Not
def CheckWin():
    global Game

    # Horizontal winning condition
    if(board[1] == board[2] and board[2] == board[3] and board[1] != ' '):
        Game = Win
    elif(board[4] == board[5] and board[5] == board[6] and board[4] != ' '):
        Game = Win
    elif(board[7] == board[8] and board[8] == board[9] and board[7] != ' '):
        Game = Win

    # Vertically Winning Condition
    elif(board[1] == board[4] and board[4] == board[7] and board[1] != ' '):
         Game = Win
    elif(board[2] == board[5] and board[5] == board[8] and board[2] != ' '):
         Game = Win
    elif(board[3] == board[6] and board[6] == board[9] and board[3] != ' '):
         Game = Win

    # Diagonal Winning Condition
    elif(board[1] == board[5] and board[5] == board[9] and board[1] != ' '):
        Game = Win
    elif(board[3] == board[5] and board[5] == board[7] and board[3] != ' '):
        Game=Win

    # MAtch Tie Or Draw Condition
    elif(board[1] !=' 'and board[2] !=' ' and board[3] !=' ' and board[4] !=' ' and board[5] !=' ' and board[6] !=' ' and board[7] !=' ' and board[8] !=' ' and board[9] !=' '):
        Game=Draw
    else:
        Game=Running

print(" Tic-Tac-Toe Game ")
print(" Player 1 [X] --- Player 2 [O]\n")
print()
print(" Please Wait...")
time.sleep(1)
while(Game == Running):
    os.system('cls')
    DrawBoard()
    if(player % 2 != 0):
        print(" Player 1's Chance")
        Mark = 'X'
    else:
        print(" Player 2's Chance")
        Mark = 'O'
    choice = int(input("Enter the Position Between [1-9] where you want to mark :"))
    if(CheckPosition(choice)):
        board[choice] = Mark
        player+=1
        CheckWin()

os.system('cls')
DrawBoard()
if(Game==Draw):
    print("Game Draw")
elif(Game==Win):
        player-=1
        if(player%2!=0):
            print("Player 1 Won")
        else:
                print("Player 2 Win")
            
