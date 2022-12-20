# Settings
gameSpeed = 1
gameRounds = 6
sidedDice = 6

"""
    How the game works:
    * Each player goes one at a time automatically. The game lasts 6 rounds by default (Without a draw.) rolling a 6 sided dice by default.
        * "gameSpeed" - Change how quickly the game moves on. (Seconds.)
        * "gameRounds" - Change how many rounds you want to play in the game.
        * "sidedDice" - Change the greatest number on the dice.
    * Each player within in their turn rolls the dice twice.
        * If the 2 dices add up and the number is even, the player gets 10 points added to their score.
        * If the 2 dices add up and the number is odd, the player gets 5 points taken away from their score unless their score is less then 5 there is no change to their score.
        * If the players dice end up both equal to eachother they roll another dice, those values from those 3 dices add up to their score
    * At the end of the game, the player with the most points win.
    * If both players end up with equal amount of points they both roll the dice once and whoever the gets the highest number within that roll wins.
    * If both players again end up with equal amount of points in the re-roll, they both roll the dice again until one person gets the greater number and is appointed winner.
"""

import random
import time

player1 = input("Enter player 1 username: ")
player2 = input("Enter player 2 username: ")
player1Total = 0
player2Total = 0

def RollDice(player):
    global player1Total
    global player2Total

    print("------", player, "TURN ------")
    time.sleep(gameSpeed)
    for dice in range(1, 3):
        roll = random.randint(1, sidedDice)
        print("Rolling", player, "dice...", roll)
        time.sleep(gameSpeed)
        if dice == 1:
            roll1 = roll
        elif dice == 2:
            roll2 = roll
            if roll1 == roll2:
                roll3 = random.randint(1, sidedDice)
                if player == player1: player1Total = player1Total + roll1 + roll2 + roll3
                else: player2Total = player2Total + roll1 + roll2 + roll3
                print("Rolling", player, "dice again...", roll3)
                time.sleep(gameSpeed)
            else:
                if (roll1 + roll2) % 2 == 0:
                    if player == player1: player1Total = player1Total + 10
                    else: player2Total = player2Total + 10
                else:
                    if player == player1:
                        if player1Total >= 5: player1Total = player1Total -5
                    else: 
                        if player2Total >= 5: player2Total = player2Total -5
    if player == player1: print(player, "total:", player1Total)
    else: print(player, "total:", player2Total)
    time.sleep(gameSpeed)

for round in range(1, gameRounds + 1):
    RollDice(player1)
    RollDice(player2)
    print("------ END OF ROUND:", round, "------")
    time.sleep(gameSpeed)

print("------ RESULT ------")
time.sleep(gameSpeed)
if player1Total > player2Total: 
    print(player1, "wins by:", player1Total - player2Total, "point/s")
elif player2Total > player1Total: 
    print(player2, "wins by:", player2Total - player1Total, "point/s")
else:
    print("------ DRAW ------")
    while True:
        for dice in range(1, 3):
            roll = random.randint(1, sidedDice)
            if dice == 1:
                player1Total = player1Total + roll
                print("Rolling", player1, "dice...", roll)
                time.sleep(gameSpeed)
            elif dice == 2:
                player2Total = player2Total + roll
                print("Rolling", player2, "dice...", roll)
                time.sleep(gameSpeed)
        print("------ RESULT ------")
        time.sleep(gameSpeed)
        if player1Total > player2Total:
            print(player1, "wins by:", player1Total - player2Total, "point/s")
            break
        elif player2Total > player1Total:
            print(player2, "wins by:", player2Total - player1Total, "point/s")
            break
        else: print("------ DRAW ------")
