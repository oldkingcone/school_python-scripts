#! /usr/bin/python

# addition game! 

import random
import os

# not sure if atexit ships with this server or not.
# but still fun to play with.
import atexit
# clears the previous output in the terminal
os.system('clear')
# defining loop variable
continueloop = "Y"
# todo can set it to keep score with a file, so that way
# the username and previous score can be reloaded.
score = 0
high_score = 0
total_questions = 0
# gets the users name, makes it more personal.
uname = input("[+] What is your name, young padwan?\n->")
# sets a goodbye message.
def goodbye():
	os.system('clear')
	print("[+] Farewell master,",uname,"![+]")
	print("[+] ",high_score," Was your high score. [+]")
	print("[+] You answered ",high_score," out of ",total_questions,"questions correctly!![+]")
# main chunk of the program.
while continueloop == "Y":
	total_questions = total_questions + 1
	num1 = random.randint(0,14)
	num2 = random.randint(0,24)
	correct_answer = num1 + num2
	print("[+] Add the sum of these numbers,",num1," and ",num2)
	guess = int(input("[+] Whats your guess young one?\n-> "))
	if guess == correct_answer:
		score = score + 1
		high_score = high_score + 1
		os.system('clear')
		# print("[+] Ah, using the force I see",uname)
		print("[+] Your current score is: ",high_score)
		# os.system('clear')
	else:
		score = 0
		os.system('clear')
		print("[+] The correct answer was, ",correct_answer)
		print("[+] For your mistake",uname,"your score has been reset to 0.")
		print("[+] This is not the answer you were looking for, try harder you must.")
		print("[+] Your score is currently: ",score)
		continueloop = input("[+] Would you like to play again? Y or N \n-> ").upper()
		# os.system('clear')
	if continueloop == 'N':
		atexit.register(goodbye)
    except (ValueError, RuntimeError, OSError, KeyboardInterrupt) as error:
        atexit.register(goodbye)
