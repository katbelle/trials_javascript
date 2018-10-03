"""A number-guessing game."""

# Put your code here

#Kat and Mimosa
#Guessing Game


from random import randint
# greet player
print("Hello! Welcome to the Guessing Game!")

# get player name and have them guess the secret number
name = input("What is your name? ")



best_score = 1000000000
def determine_best_score(best_score, guess_count):
	if guess_count < best_score:
		best_score = guess_count
	return best_score

def if_play_again():
	play_again = input("Do you want to play again? y or n\n")
	if play_again == "y":
		play_guessing_game(best_score)
	if play_again == "n":
		print(f"Bye, {name}. Thanks for playing!")
		return play_again
	
# guessing repeats until secret number is guessed
def play_guessing_game(best_score):
	print(f"Welcome, {name}. In this game we will ask you to guess a integer within a range of your choice.")
	guess_count = 1

	#set a range
	min = int(input("What would you like to be the lowest possible number?: "))
	max = int(input("What would you like to be the highest possible number?: "))

	# choose random number within range
	secret_number = randint(min,max+1)

	while True:
	#     get guess
	#     if guess is incorrect:
	#         give hint
		guess = input("Guess a number:")
		if guess_count > 10:
			print("You took over 10 guesses, you lose")
			if if_play_again() == "n":
				break

		try:
			guess = int(guess)

			if guess < 1 or guess >100:
				guess = input("Sorry. Please enter an integer between 1 and 100, inclusive:")
				guess = int(guess)
		
		#         increase number of guesses	
			if guess != secret_number:
				guess_count += 1
				if guess < secret_number:
					print("That's too low!")
					
				if guess > secret_number:
					print("That's too high!")
						
		#     else:
		#         congratulate player
			else:
				best_score = determine_best_score(best_score,guess_count)

				if guess_count == 1:
					print(f"Congratulations, {name}! You guessed the number with only 1 guess. That's your best score!")	
				else:
					print(f"Congratulations, {name}! You guessed the number with only {guess_count} guesses. The best score is {best_score}")
				if if_play_again() == "n":
					break
				
		except:
			print(f"{name}! Your submission was not an integer.")
			continue


play_guessing_game(best_score)



