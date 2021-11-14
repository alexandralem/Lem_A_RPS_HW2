from gameComponents import gameVars, livesCount
from colorama import init
from colorama import Fore, Back, Style
init(autoreset=True)

def comparisonfunction(computer):
        if (computer == gameVars.player):
                print(Fore.BLUE + "tie! try again")

        elif (gameVars.player == "rock"):
            if (computer == "paper"):
                print(Fore.RED + "you lose!")
                gameVars.playerLives = gameVars.playerLives -1
                livesCount.livesdisplay(gameVars.playerLives)

            else:
                print(Fore.GREEN + "you win!")

                gameVars.computerLives = gameVars.computerLives -1


        elif (gameVars.player == "paper"):
            if (computer == "scissors"):
                print("you lose!")
                gameVars.playerLives = gameVars.playerLives -1
            else:
                print("you win!")
                gameVars.computerLives = gameVars.computerLives -1


        elif (gameVars.player == "scissors"):    
            if (computer == "rock"):
                print("you lose!")
                gameVars.playerLives = gameVars.playerLives -1
            else:
                print("you win!")
                gameVars.computerLives = gameVars.computerLives -1
