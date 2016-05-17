import random 
import re 

def displayGameTitle(): 
    print("\nGame of Rock, Paper, Scissors, Lizard, Spock") 

def displayGameRules(): 
    print("\nKeyboard keys and game rules: \n\n1: Scissors cuts Paper (2) and decapitates Lizard (4) \n2: Paper covers Rock (3) and disproves Spock (5) \n3: Rock crushes Scissors (1) and crushes Lizard (4) \n4: Lizard eats Paper (2) and envenomates Spock (5) \n5: Spock vaporizes Rock (3) and smashes Scissors (1)") 

def selectGameMode(): 
    print("\nTo play against the computer, press 1 \nTo play against another player, press 2") 
    modeInput = input("\nPlease select the game mode: ") 
    modeInput = validateGameMode(modeInput) 
    if modeInput == "1": 
        selectedGameMode = "Single Player Game" 
    else: 
        selectedGameMode = "Multi Player Game"
    return selectedGameMode 

def validateGameMode(rawModeInput): 
    if re.match("^[12]$", rawModeInput): 
        return rawModeInput 
    else: 
        rawModeInput = input("\nPlease press 1 or 2: ")
        return validateGameMode(rawModeInput) 

def selectPlayerOptions(currentMode):
    player1Name = selectPlayerName(1) 
    if currentMode == "Single Player Game": 
        player2Name = "Computer" 
    else: 
        player2Name = selectPlayerName(2) 
    playerNames = [player1Name, player2Name] 
    return playerNames

def selectPlayerName(playerNumber): 
    if playerNumber == 1: 
        nameInput = input("\nPlayer 1, please enter your name: ") 
        playerName = validatePlayerName(nameInput) 
        return playerName 
    else: 
        nameInput = input("\nPlayer 2, please enter your name: ") 
        playerName = validatePlayerName(nameInput) 
        return playerName 

def validatePlayerName(rawNameInput): 
    if len(rawNameInput) < 2: 
        print("Player name must contain 2 characters or more") 
        rawNameInput = input("Please enter your name: ")
        return validatePlayerName(rawNameInput) 
    elif len(rawNameInput) > 20: 
        print("Player name must contain 20 characters or less") 
        rawNameInput = input("Please enter your name: ") 
        return validatePlayerName(rawNameInput)
    elif re.match("^[a-zA-Z0-9\s]*$", rawNameInput): 
        return rawNameInput 
    else: 
        print("Player name must contain only letters, numbers, or spaces") 
        rawNameInput = input("Please enter your name: ")
        return validatePlayerName(rawNameInput) 

def startPlayingGame(currentMode, currentPlayers, currentScore): 
        player1Hand = selectPlayerHand(currentPlayers[0]) 
        if currentMode == "Single Player Game": 
            gameHands = [1, 2, 3, 4, 5] 
            player2Hand = random.choice(gameHands) 
        else: 
            player2Hand = selectPlayerHand(currentPlayers[1]) 
        roundResult = figureHandResult(player1Hand, player2Hand) 
        roundScore = updateScoreBoard(roundResult, currentPlayers[0], currentPlayers[1], player1Hand, player2Hand, currentScore[0], currentScore[1]) 
        print("\n" + currentPlayers[0], str(roundScore[0]) + ":" + str(roundScore[1]), currentPlayers[1])
        nextRound = playNextRound() 
        if nextRound == "y": 
            print("\033c") 
            return startPlayingGame(currentMode, currentPlayers, roundScore) 
        else: 
            print("\033c") 
            return roundScore

def selectPlayerHand(currentPlayerName):
    print("\nPlease select your hand") 
    handInput = input(currentPlayerName + ", press any key from 1 to 5: ") 
    playerHand = validatePlayerHand(handInput)
    print("\033c") 
    return playerHand 

def validatePlayerHand(rawHandInput): 
    if re.match("^[1-5]$", rawHandInput): 
        rawHandInput = int(rawHandInput) 
        return rawHandInput 
    else: 
        rawHandInput = input("Please press any key from 1 to 5: ")
        return validatePlayerHand(rawHandInput) 

def figureHandResult(currentHand1, currentHand2):
    if (currentHand2 - currentHand1) % 5 in (1, 3): 
        winningHand = "Player 1" 
    elif (currentHand2 - currentHand1) % 5 in (2, 4): 
        winningHand = "Player 2" 
    else: 
        winningHand = "Tie" 
    return winningHand

def updateScoreBoard(result, player1, player2, hand1, hand2, score1, score2):
    handTitleList = ["Scissors", "Paper", "Rock", "Lizard", "Spock"] 
    handMessageList = ["Scissors (1) cuts Paper (2)", "Paper (2) covers Rock (3)", "Rock (3) crushes Lizard (4)", "Lizard (4) poisons Spock (5)", "Spock (5) smashes Scissors (1)", "Scissors (1) decapitates Lizard (4)", "Lizard (4) eats Paper (2)", "Paper (2) disproves Spock (5)", "Spock (5) vaporizes Rock (3)", "Rock (3) crushes Scissors (1)"]
    handTitle1 = handTitleList[hand1 - 1] 
    handTitle2 = handTitleList[hand2 - 1] 
    print(player1 + " selected " + handTitle1 + "(" + str(hand1) + ")") 
    print(player2 + " selected " + handTitle2 + "(" + str(hand2) + ")") 
    if (hand1 == 1 and hand2 == 2) or (hand1 == 2 and hand2 == 1): 
        print("\n" + handMessageList[0]) 
    elif (hand1 == 2 and hand2 == 3) or (hand1 == 3 and hand2 == 2): 
        print("\n" + handMessageList[1]) 
    elif (hand1 == 3 and hand2 == 4) or (hand1 == 4 and hand2 == 3): 
        print("\n" + handMessageList[2]) 
    elif (hand1 == 4 and hand2 == 5) or (hand1 == 5 and hand2 == 4): 
        print("\n" + handMessageList[3]) 
    elif (hand1 == 5 and hand2 == 1) or (hand1 == 1 and hand2 == 5): 
        print("\n" + handMessageList[4]) 
    elif (hand1 == 1 and hand2 == 4) or (hand1 == 4 and hand2 == 1): 
        print("\n" + handMessageList[5]) 
    elif (hand1 == 4 and hand2 == 2) or (hand1 == 2 and hand2 == 4): 
        print("\n" + handMessageList[6]) 
    elif (hand1 == 2 and hand2 == 5) or (hand1 == 5 and hand2 == 2): 
        print("\n" + handMessageList[7]) 
    elif (hand1 == 5 and hand2 == 3) or (hand1 == 3 and hand2 == 5): 
        print("\n" + handMessageList[8]) 
    elif (hand1 == 3 and hand2 == 1) or (hand1 == 1 and hand2 == 3): 
        print("\n" + handMessageList[9]) 
    else: 
        print("\nPlayers picked the same hand") 
    if result == "Player 1": 
        print("\n" + player1 + " is the winner!") 
        score1 += 1 
    elif result == "Player 2": 
        print("\n" + player2 + " is the winner!") 
        score2 += 1 
    else: 
        print("\nThe game is tied!") 
    updatedScore = [score1, score2] 
    return updatedScore 

def playNextRound():
    print("\nWould you like to play another round?") 
    nextRoundChoice = input("Please press y or n on the keyboard: ") 
    nextRoundChoice = validateNextRoundInput(nextRoundChoice) 
    return nextRoundChoice

def validateNextRoundInput(nextRoundInput):
    if re.match("^[yn]$", nextRoundInput): 
        return nextRoundInput 
    else: 
        nextRoundInput = input("Please press y or n to continue or stop: ") 
        return validateNextRoundInput(nextRoundInput) 

def displayFinalScore(currentPlayers, finalScore): 
    print("Game over!\n\n" + currentPlayers[0], str(finalScore[0]) + ":" + str(finalScore[1]), currentPlayers[1] + "\n")

def main(): 
    displayGameTitle() 
    displayGameRules()
    gameMode = selectGameMode() 
    print("\033c")
    print(gameMode)
    players = selectPlayerOptions(gameMode)
    gameScore = [0, 0] 
    print("\033c") 
    print(gameMode)
    print("\n" + players[0], str(gameScore[0]) + ":" + str(gameScore[1]), players[1]) 
    gameScore = startPlayingGame(gameMode, players, gameScore) 
    displayFinalScore(players, gameScore) 

main()