from random import randint


# an array is just a container. It holds multiple values in a 0-based index
# you can store anything in an array and retrieve it later. Arrays have square brackets notation
choices = ["rock", "paper", "scissors"]

#add player and computer lives
#Boolean values are True or False - you can use these to check state 
player = False
playerLives = 2
computerLives = 2

# create an infinite loop (for now) so that we can keep playing
while player is False:

        player = input("Choose rock, paper or scissors: ")
        computer = choices[randint (0,2)]
        print ("player chose:" + player)
        print ("computer chose: " + computer)

        if (computer == player):
                print("tie! try again")

        elif (player == "rock"):
            
            if (computer == "paper"):
                print("you lose!")
                playerLives = playerLives -1
            else:
                print("you win!")
                computerLives = computerLives -1


        elif (player == "paper"):
            if (computer == "scissors"):
                print("you lose!")
                playerLives = playerLives -1
            else:
                print("you win!")
                computerLives = computerLives -1


        elif (player == "scissors"):    
            if (computer == "rock"):
                print("you lose!")
                playerLives = playerLives -1
            else:
                print("you win!")
                computerLives = computerLives -1

        print("computer lives: " + str(computerLives))
        print("player lives: " + str(playerLives))

        player = False

        
        if playerLives == 0:
            print("you lost! would you like to play again?")
            choice = input(" Y / N? ")

            if choice == "n":
                print("better luck next time!")
                exit()
            else:
                # reset and restart the game
                playerLives = 5
                computerLives = 5
                player = False


        elif computerLives == 0:
            print("you won! would you like to play again?")
            choice = input(" Y / N? ")

            if choice == "n":
                print("better luck next time!")
                exit()
            else:
                # reset and restart the game
                playerLives = 5
                computerLives = 5
                player = False

        




