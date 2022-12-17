import random
import pandas as pd

playerName = None
playerAction = None
lastPlayerAction = None
computerAction = None
lastComputerAction = None
winner = None
turn = 0
chooseAction = {'ROCK':'PAPER', 'PAPER':'SCISSORS', 'SCISSORS':'ROCK'}
resultsFrame = pd.DataFrame()

while True:
    if playerName == None:
        playerName = input("Player, What is your name? ")

    while True:
        playerAction = input(str(playerName) + ", what is your play? ")

        if playerAction.upper() not in chooseAction:
            print("Action not recognized, please try again!")
            print('\n')
        else:
            break

    if turn <= 11:
        computerAction = random.choice(list(chooseAction.keys()))

    print('\n')
    print('I play: ' + str(computerAction) + ' You play: ' + str(playerAction.upper()))

    if computerAction.upper() == chooseAction[playerAction.upper()]:
        print('I win!')
        winner = 'COM'
    elif playerAction.upper() == chooseAction[computerAction.upper()]:
        print('You win!')
        winner = 'PLAYER'
    elif computerAction.upper() == playerAction.upper():
        print('Tie!')
        winner = 'TIE'
    print('\n')

    resultsList = [playerName.upper(), turn, playerAction.upper(), computerAction, winner, lastPlayerAction, lastComputerAction]
    resultsFrame = resultsFrame.append(pd.DataFrame(resultsList).T)

    turn += 1

    lastPlayerAction = playerAction.upper()
    lastComputerAction = computerAction