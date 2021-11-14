from random import randint
from gameComponents import winLose, gameVars
from gameComponents import comparison


# an array is just a container. It holds multiple values in a 0-based index
# you can store anything in an array and retrieve it later. Arrays have square brackets notation


# define a win/lose function and invoke it in our game loop when lives run out (player or computer)

# create an infinite loop (for now) so that we can keep playing
while gameVars.player is False:
        gameVars.player = input("Choose rock, paper or scissors: ")
        computer = gameVars.choices[randint (0,2)]

        comparison.comparisonfunction(computer)

        print ("player chose:" + gameVars.player)
        print ("computer chose: " + computer)

        print("computer lives: " + str(gameVars.computerLives))
        print("player lives: " + str(gameVars.playerLives))

        if gameVars.playerLives == 0:
            # call the winorlose function here
            winLose.winorlose("lost")


        elif gameVars.computerLives == 0:
            # call the winorlose function here
            winLose.winorlose("won")

        gameVars.player = False
