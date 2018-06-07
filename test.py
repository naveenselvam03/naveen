# --- MASTERMIND --- #

import random

print (" --- MASTERMIND --- \n")
print ("Guess the secret number code in as few tries as possible.\n")
print ("Please, enter four numbers")

numbers = ["1", "2", "3", "4", "5", "6"]
attempts = 0
game = True

# computer randomly picks four-number code
number_code = random.sample(numbers,4)	
print (number_code)

# player guesses the number	
while game:
	correct_number = ""
	guessed_number = ""
	player_guess = input().upper()
	attempts += 1
	
	# checking if player's input is correct
	if len(player_guess) != len(number_code):
		print ("\nThe secret code has exactly four numbers. I know, you can count to four. Try again!")
		continue
	for i in range(4):
		if player_guess[i] not in numbers:
			print ("\nLook up what numbers you can use in this game. You are not a daltonist, are you?")
			continue
			
	# comparison between player's input and secret code
	if correct_number != "XXXX":
		for i in range(4):
			if player_guess[i] == number_code[i]:
				correct_number += "1"
			if  player_guess[i] != number_code[i] and player_guess[i] in number_code:
				guessed_number += "O"
		print (correct_number +  guessed_number + "\n")		
		
	if correct_number == "XXXX":
		if attempts == 1:
			print ("Wow! You guessed at the first attempt!")
		else:
			print ("Well done... You needed " + str(attempts) + " attempts to guess.")
		game = False
		
	if attempts >= 1 and attempts <8 and correct_number != "XXXX":
		print ("Next attempt: ")
	elif attempts >= 8:
		print ("You didn't guess! The secret color code was: " + str(number_code))	

	# play or not to play
	while game == False:
		finish_game = input("\nDo you want to play again (Y/N)?").upper()	
		attempts = 0
		if finish_game =="N":
			print ("Thanks for the game! Bye, bye!")
		elif finish_game == "Y":
			game = True
			print ("So, let's play again... Guess the secret code: ")

# --- end --- #			
