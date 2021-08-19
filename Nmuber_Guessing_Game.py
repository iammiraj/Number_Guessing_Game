# Number Guessing Game

import random

print('\nWelcome To The Number Guessing Game\n')

def gameMenu ():
	print('START THE GAME? [Y/N]')
	start = input()

	if start == "Y":
		playGame()
		
	elif start == "y":
		playGame()
		
	else:
		gameMenu()

def playGame ():
	print('\nLevels')
	print('# Easy   [Type 1]')
	print('# Medium [Type 2]')
	print('# Hard   [Type 3]')
	print('\nChoose Difficulty Level:')

	level = input()
	level = int(level)

	if level == 1:
		number = random.randint(1, 10)
		range = 10
		
	elif level == 2:
		number = random.randint(1, 50)
		range = 50
		
	elif level == 3:
		number = random.randint(1, 100)
		range = 100

	print('\nEnter your name?')
	name = input()
	print('\nHello, ' + name + '! I am thinking of a number between 1 and '+str(range)+'.')
	print('\nYou will have 5 guesses.')

	guessesTaken = 0
	guessesLeft = 5
	attempt = 1
	hintLeft = 1

	while guessesTaken < 5:
		print('\n¤ Attempt '+str(attempt)+': Take a guess_ [You have '+str(guessesLeft)+' guesses & '+str(hintLeft)+' hint left.]')
		guess = input()
		guess = int(guess)

		guessesTaken = guessesTaken + 1
		guessesLeft = guessesLeft - 1
		attempt = attempt + 1

		if guess < number:
			print('Your guess was low.')
			if hintLeft > 0:
				print('\nDo you want a hint ? [Y/N]')
				hint = input()				
				if hint == "Y":
					hintLeft = hintLeft - 1					
					if number % 2 == 0:
						print('Hint: The number is even.')						
					else:
						print('Hint: The number is odd.')
				elif hint == "y":
					hintLeft = hintLeft - 1				
					if number % 2 == 0:
						print('Hint: The number is even.')
					else:
						print('Hint: The number is odd.')

		elif guess > number:
			print('Your guess was high.')
			if hintLeft > 0:
				print('\nDo you want a hint ? [Y/N]')
				hint = input()
				if hint == "Y":
					hintLeft = hintLeft - 1
					if number % 2 == 0:
						print('Hint: The number is even.')
					else:
						print('Hint: The number is odd.')
				elif hint == "y":
					hintLeft = hintLeft - 1
					if number % 2 == 0:
						print('Hint: The number is even.')
					else:
						print('Hint: The number is odd.')

		elif guess == number:
			break

	if guess == number:
		guessesTaken = str(guessesTaken)
		print('\nWell done, ' + name + '! You guessed my number in ' + guessesTaken + ' guesses.\n')

	if guess != number:
		number = str(number)
		print('\nNope. The number I was thinking of was ' + number+'.\n')
		
	main()

def main ():
	gameMenu()
	playGame()

main()
