from random import randint
from gameComponents import winLose, gameVars, livesCount
from gameComponents import comparison


while gameVars.player is False:
        gameVars.player = input("Choose rock, paper or scissors: ")
        computer = gameVars.choices[randint (0,2)]

        comparison.comparisonfunction(computer)

        print ("======player chose:" + gameVars.player + "======")
        print ("======computer chose: " + computer + "======")

        print("computer lives: " + str(gameVars.computerLives))
        livesCount.computerlivesdisplay(gameVars.computerLives)

        print("player lives: " + str(gameVars.playerLives))
        livesCount.playerlivesdisplay(gameVars.playerLives)

        if gameVars.playerLives == 0:
            winLose.winorlose("lost")


        elif gameVars.computerLives == 0:
            winLose.winorlose("won")

        gameVars.player = False
