def validateModeInput(rawModeInput): 
    import re
    if re.match("^[12]$", rawModeInput): 
        validModeInput = rawModeInput 
        return validModeInput 
    else: 
        rawModeInput = input("Please press 1 or 2 to select the game mode: ")
        return validateModeInput(rawModeInput)

def selectGameMode(): 
    print("To play against computer, press 1") 
    print("To play against another player, press 2") 
    rawModeSelection = input("Please select the game mode: ") 
    validModeSelection = validateModeInput(rawModeSelection) 
    if validModeSelection is "1": 
        return "Single Player Game" 
    else: 
        return "Multi Player Game" 

def validateNameInput(rawNameInput): 
    import re
    if len(rawNameInput) < 2: 
        print("The selected name is too short! \nIt must contain 2 characters or more.") 
        rawNameInput = input("Please enter your name: ")
        return validateNameInput(rawNameInput) 
    elif len(rawNameInput) > 20: 
        print("The selected name is too long! \nIt must contain 20 characters or less.") 
        rawNameInput = input("Please enter your name: ")
        return validateNameInput(rawNameInput) 
    elif re.match("^[a-zA-Z0-9\s]*$", rawNameInput): 
         return rawNameInput 
    else: 
        print("The selected name contains special characters. \nIt must contain letters, numbers, or spaces.") 
        rawNameInput = input("Please enter your name: ")
        return validateNameInput(rawNameInput) 

def selectPlayerNames(currentGameMode): 
    print(currentGameMode) 
    if currentGameMode == "Single Player Game": 
        rawPlayer1Name = input("Player 1, please enter your name: ") 
        validPlayer1Name = validateNameInput(rawPlayer1Name) 
        validPlayer2Name = "Computer" 
        validPlayerNames = [validPlayer1Name, validPlayer2Name] 
        return validPlayerNames 
    else: 
        rawPlayer1Name = input("Player 1, please enter your name: ") 
        validPlayer1Name = validateNameInput(rawPlayer1Name) 
        rawPlayer2Name = input("Player 2, please enter your name: ") 
        validPlayer2Name = validateNameInput(rawPlayer2Name) 
        validPlayerNames = [validPlayer1Name, validPlayer2Name] 
        return validPlayerNames 

def gameMenu(): 
    print("Menu") 
    selectedGameMode = selectGameMode() 
    gamePlayData = [selectedGameMode] 
    selectedPlayerNames = selectPlayerNames(selectedGameMode) 
    gamePlayData.extend(selectedPlayerNames) 
    return gamePlayData 

def validatePlayerHand(rawHandInput): 
    import re
    if re.match("^[1-5]$", rawHandInput): 
        validHandInput = int(rawHandInput) 
        return validHandInput 
    else: 
        rawHandInput = input("Please press any key from 1 to 5 to pick your hand: ")
        return validatePlayerHand(rawHandInput) 

def validatePlayAgainInput(rawPlayInput): 
    import re
    if re.match("^[yn]$", rawPlayInput): 
        validPlayInput = rawPlayInput 
        return validPlayInput 
    else: 
        rawPlayInput = input("Please press y or n to continue or stop: ") 
        return validatePlayAgainInput(rawPlayInput) 

def gamePlay(playData, player1Score, player2Score): 
    gameMode = playData[0] 
    print("\n" + gameMode) 
    player1Name = playData[1] 
    player2Name = playData[2] 
    print(player1Name, player1Score, ":", player2Score, player2Name) 
    print("\nGame Rules \n\nPick your hand by pressing any of \nthe following keys on your keyboard. \n\n1: Scissors cuts Paper (2) and decapitates Lizard (4) \n2: Paper covers Rock (3) and disproves Spock (5) \n3: Rock crushes Scissors (1) and crushes Lizard (4) \n4: Lizard eats Paper (2) and envenomates Spock (5) \n5: Spock vaporizes Rock (3) and smashes Scissors (1)") 
    rawPlayer1Hand = input(player1Name + ", pick your hand: ")
    print("\033c") 
    validPlayer1Hand = validatePlayerHand(rawPlayer1Hand) 
    if gameMode == "Single Player Game": 
        import random 
        gameHands = [1, 2, 3, 4, 5]
        validPlayer2Hand = random.choice(gameHands) 
    else: 
        print("\nGame Rules \n\nPick your hand by pressing any of \nthe following keys on your keyboard. \n\n1: Scissors cuts Paper (2) and decapitates Lizard (4) \n2: Paper covers Rock (3) and disproves Spock (5) \n3: Rock crushes Scissors (1) and crushes Lizard (4) \n4: Lizard eats Paper (2) and envenomates Spock (5) \n5: Spock vaporizes Rock (3) and smashes Scissors (1)") 
        rawPlayer2Hand = input(player2Name + ", pick your hand: ") 
        print("\033c") 
        validPlayer2Hand = validatePlayerHand(rawPlayer2Hand) 
    if (validPlayer2Hand - validPlayer1Hand) % 5 in (1, 3): 
        print("The winner is", player1Name + "!") 
        player1Score += 1 
    elif (validPlayer2Hand - validPlayer1Hand) % 5 in (2, 4): 
        print("The winner is", player2Name + "!") 
        player2Score += 1 
    else: 
        print("The game is a tie!") 
    gameHandList = ["Scissors", "Paper", "Rock", "Lizard", "Spock"]
    player1Hand = gameHandList[validPlayer1Hand - 1] 
    player2Hand = gameHandList[validPlayer2Hand - 1] 
    print(player1Name, "selected", player1Hand) 
    print(player2Name, "selected", player2Hand) 
    print(player1Name, player1Score, ":", player2Score, player2Name) 
    print("\nWould you like to continue playing? \nPlease press y for yes and n for no.") 
    rawPlayAgainChoice = input("Please press y or n on the keyboard: ") 
    validPlayAgainChoice = validatePlayAgainInput(rawPlayAgainChoice) 
    gameTotalScore = [player1Score, player2Score] 
    if validPlayAgainChoice == "y": 
        return gamePlay(playData, player1Score, player2Score) 
    else: 
        print("Game over!") 
        return gameTotalScore

def scoreBoard(scoreBoardData, totalScore): 
    finalPlayer1Name = scoreBoardData[1] 
    finalPlayer2Name = scoreBoardData[2]
    finalScore1 = totalScore[0] 
    finalScore2 = totalScore[1] 
    print(finalPlayer1Name, finalScore1, ":", finalScore2, finalPlayer2Name)

def main(): 
    print("\nGame of Rock, Paper, Scissors, Lizard, Spock") 
    combinedGamePlayData = gameMenu() 
    player1CurrentScore = 0 
    player2CurrentScore = 0 
    finalTotalScore = gamePlay(combinedGamePlayData, player1CurrentScore, player2CurrentScore) 
    scoreBoard(combinedGamePlayData, finalTotalScore) 

main() 