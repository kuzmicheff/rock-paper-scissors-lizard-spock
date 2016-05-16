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
    rawModeSelection = input("Plese select the game mode: ") 
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

def selectPlayerName(currentGameMode): 
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
    selectedPlayerNames = selectPlayerName(selectedGameMode) 
    gamePlayData.extend(selectedPlayerNames) 
    return gamePlayData 

def singlePlayerGame(): 
    pass

def multiPlayerGame(): 
    pass

def gamePlay(playData, player1Score, player2Score): 
    print(playData, player1Score, player2Score) 

def scoreBoard():
    pass

def main(): 
    print("Game of Rock, Paper, Scissors, Lizard, and Spock") 
    combinedGamePlayData = gameMenu() 
    player1CurrentScore = 0 
    player2CurrentScore = 0 
    gamePlay(combinedGamePlayData, player1CurrentScore, player2CurrentScore) 
#    scoreBoard()  

main() 