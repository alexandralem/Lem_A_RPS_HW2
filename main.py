from random import randint

#add player and computer lives
playerLives = 5
computerLives = 5

player = input("Choose rock, paper or scissors: ")
print ("player chose:" + player)

# an array is just a container. It holds multiple values in a 0-based index
# you can store anything in an array and retrieve it later. Arrays have square brackets notation
choices = ["rock", "paper", "scissors"]

computer = choices[randint (0,2)]

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