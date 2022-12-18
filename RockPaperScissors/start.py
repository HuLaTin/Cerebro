import random
import pandas as pd

playerName = None
playerAction = None
lastPlayerAction = None
computerAction = None
lastComputerAction = None
winner = None
turn = 1
chooseAction = {'ROCK':'PAPER', 'PAPER':'SCISSORS', 'SCISSORS':'ROCK'}
resultsFrame = pd.DataFrame()

while True:
    rockChoice = 0
    paperChoice = 0
    scissorsChoice = 0
    didWin = 0

    if playerName == None:
        playerName = input("Player, What is your name? ")

    while True:
        playerAction = input(str(playerName) + ", what is your play? ")

        if playerAction.upper() not in chooseAction:
            print("Action not recognized, please try again!")
            print('\n')
        else:
            break

    # if turn <= 11:
    #     computerAction = random.choice(list(chooseAction.keys()))

    computerAction = random.choice(list(chooseAction.keys()))


    print('\n')
    print('I play: ' + str(computerAction) + ' || You play: ' + str(playerAction.upper()))


    if computerAction.upper() == chooseAction[playerAction.upper()]:
        print('I win!')
        didWin = 1
        winner = 'COM'
    elif playerAction.upper() == chooseAction[computerAction.upper()]:
        print('You win!')
        winner = 'PLAYER'
    elif computerAction.upper() == playerAction.upper():
        print('Tie!')
        winner = None
    print('\n')

    if playerAction.upper() == 'ROCK':
        rockChoice = 1
    elif playerAction.upper() == 'PAPER':
        paperChoice = 1
    elif playerAction.upper() == 'SCISSORS':
        scissorsChoice = 1

    try:
        winRate = (sum(resultsFrame[7]) + didWin) / turn
    except:
        winRate = didWin / turn

    print("My win percentage: " + str(int(winRate * 100)) + '%')



    resultsList = [playerName.upper(), turn, playerAction.upper(), computerAction, winner, lastPlayerAction, lastComputerAction, didWin, rockChoice, paperChoice, scissorsChoice]
    #outputxlsx = pd.concat([outputxlsx, df])

    #resultsFrame = resultsFrame.append(pd.DataFrame(resultsList).T)
    resultsFrame = pd.concat([resultsFrame, pd.DataFrame(resultsList).T])

    if len(resultsFrame) == 101:
        resultsSmall = resultsFrame.iloc[1:,2:]
        resultsFrame.to_csv(r'RockPaperScissors\results.csv')

    turn += 1

    lastPlayerAction = playerAction.upper()
    lastComputerAction = computerAction