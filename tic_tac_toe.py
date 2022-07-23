"""
Game Rules
Traditionally the first player plays with "X". So you can decide who wants to go with "X" and who wants to go with "O".
Only one player can play at a time.
If any of the players have filled a square then the other player and the same player cannot override that square.
There are only two conditions that may match will be draw or may win.
The player that succeeds in placing three respective marks (X or O) in a horizontal, vertical, or diagonal row wins the game.
Winning condition

Whoever places three respective marks (X or O) horizontally, vertically, or diagonally will be the winner.
"""

import os
import time

print("Tic-Tac-Toe Game Designed By Vraj thakar")
pl1 = str(input("player1 name: "))
pl2 = str(input("player2 name: "))
v = 2

def ask():
    v = int(input("would you like to play again? press '1' for NO and '2' for yes: "))
    if v == 1:
        print("have a good day, bye")
        exit()
    else:
        print("please wait.....")
        time.sleep(2)

while v == 2:

    board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']  # take 10 empty palce due to zero based indexing
    player = 1

    # ---- indicater---
    win = 0
    draw = 1
    running = 2
    stop = 3
    # ------------
    game = running
    mark = "x"


    # this function draw game boards

    def Drawbords():
        print(" %c | %c | %c " % (board[1], board[2], board[3]))
        print("___|___|___")
        print(" %c | %c | %c " % (board[4], board[5], board[6]))
        print("___|___|___")
        print(" %c | %c | %c " % (board[7], board[8], board[9]))
        print("   |   |   ")


    # this function check position is empty or not
    def checkposition(x):
        if board[x] == ' ':
            return True
        else:
            return False


    # this function checks player has won or not

    def checkwin():
        global game
        # horizontal winning condition
        if board[1] == board[2] and board[2] == board[3] and board[1] and board[1] != ' ':
            game = win
        elif board[4] == board[5] and board[5] == board[6] and board[4] and board[4] != ' ':
            game = win
        elif board[7] == board[8] and board[8] == board[9] and board[9] and board[7] != ' ':
            game = win
        # Vertical Winning Condition
        elif board[1] == board[4] and board[4] == board[7] and board[1] != ' ':
            game = win
        elif board[2] == board[5] and board[5] == board[8] and board[2] != ' ':
            game = win
        elif board[3] == board[6] and board[6] == board[9] and board[3] != ' ':
            game = win
        # Diagonal Winning Condition
        elif board[1] == board[5] and board[5] == board[9] and board[5] != ' ':
            game = win
        elif board[3] == board[5] and board[5] == board[7] and board[5] != ' ':
            game = win  # 1
        # match tie or draw condition
        elif board[1] != ' ' and board[2] != ' ' and board[3] != ' ' and board[4] != ' ' and board[5] != ' ' and board[
            6] != ' ' and board[7] != ' ' and board[8] != ' ' and board[9] != ' ':
            game = draw  # -1
        else:
            game = running  # 0


# executing part
    print(f"{pl1} [X] --- {pl2} [O]\n")
    print()
    print()
    print("Please Wait...")
    time.sleep(3)

    while game == running:
        os.system('cls')
        print()
        Drawbords()
        if player % 2 != 0:
            print(f"{pl1}'s chance")
            Mark = 'X'
        else:
            print(f"{pl2}'s chance")
            Mark = 'O'
        choice = int(input("Enter the position between [1-9] where you want to mark : "))
        if choice>9:
            print("Try again")
            continue

        elif checkposition(choice):
            board[choice] = Mark
            player += 1
            checkwin()

    os.system('cls')
    print()
    Drawbords()
    if game == draw:
        print("Game Draw")
    elif game == win:
        player -= 1
        if player % 2 != 0:
            print(f"{pl1} Won")
            ask()
        else:
            print(f"{pl2}Won")
            print("Thank you!")
            ask()
