# IPND Stage 2 Final Project

# You've built a Mad-Libs game with some help from Sean.
# Now you'll work on your own game to practice your skills and demonstrate what you've learned.

# For this project, you'll be building a Fill-in-the-Blanks quiz.
# Your quiz will prompt a user with a paragraph containing several blanks.
# The user should then be asked to fill in each blank appropriately to complete the paragraph.
# This can be used as a study tool to help you remember important vocabulary!

# Note: Your game will have to accept user input so, like the Mad Libs generator,
# you won't be able to run it using Sublime's `Build` feature.
# Instead you'll need to run the program in Terminal or IDLE.
# Refer to Work Session 5 if you need a refresher on how to do this.

# To help you get started, we've provided a sample paragraph that you can use when testing your code.
# Your game should consist of 3 or more levels, so you should add your own paragraphs as well!


# Quiz bank
easy_quiz = '''In this stage, you will use the ___1___ programming language to build your own ___2___. 
You will use a fill-in-the blank style to ___3___ a ___2___ that can even be used as a study tool 
to help you remember important ___4___.'''
easy_answer = ['Python', 'quiz', 'creat', 'vocabulary']

medium_quiz = '''For this ___1___, you'll be building a Fill-in-the-Blanks ___2___.
Your ___2___ will prompt a user with a paragraph containing several ___3___s.
The user should then be asked to fill in each blank appropriately to complete the paragraph.
This can be used as a study tool to help you remember important ___4___!'''
medium_answer = ['project', 'quiz', 'blank', 'vocabulary']

hard_quiz = '''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
tuple, and ___4___ or can be more complicated such as objects and lambda functions.'''
hard_answer = ['function', 'variables', 'nothing', 'list']

white_blanks = ['___1___', '___2___', '___3___', '___4___']
#white_blanks = ['___1___', '___2___', '___3___', '___4___', '___5___', \
#				'___6___', '___7___', '___8___', '___9___', '___10___']

# Print language bank
welcome = "*" * 50 + "\n" + "  Welcome to this quiz. \n  Please select difficulty by typing it in." + "\n" + "*" * 50
congratulation = "*" * 50 + "\n" + "  Congratulation! You have completed this quiz! " + "\n" + "*" * 50
sorry = "*" * 50 + "\n" + "  Sorry! You lost the game! " + "\n" + "*" * 50

# Check the answer
def check_answer(user_input_answer, answer, index_blank):
	if user_input_answer == answer[index_blank]:
		return 'Correct'
	else:
		return 'Incorrect'

#1 welcome, slect level
print welcome
levels = ['easy', 'medium', 'hard']
user_input_level = raw_input( "Possible choices are easy, medium, and hard: "" ")

#2 Choose level: easy, medium, hard. Return: level, quiz, answer.
def level_chosen(user_input_level):
	while user_input_level not in levels:
		user_input_level = raw_input( "Wrong input! \nPossible choices are easy, medium, and hard: "" ")
	if user_input_level == 'easy':
		return easy_quiz, easy_answer, 'easy'
	if user_input_level == 'medium':
		return medium_quiz, medium_answer, 'medium'
	else:
		return hard_quiz, hard_answer , 'hard'

level_chosen_results = level_chosen(user_input_level)

print ("\n" + "You've chosen " + level_chosen_results[2] + " difficulty." +"\n")
print ("You will get 5 guesses per problem." + "\n")
print ("The quiz is: ")
print (level_chosen_results[0] + "\n")

#3 The game body
def fill_in_blanks():
	quiz = level_chosen_results[0]
	answer = level_chosen_results[1]
	index_blank = 0
	num_try = 1
	while index_blank < len(white_blanks) and num_try < 5:
		num_try = 1 # try number reset
		user_input_answer = raw_input("What should be filled in for " + str(white_blanks[index_blank]) + "? ")
		while check_answer(user_input_answer, answer, index_blank) == 'Incorrect' and num_try < 5:
			print "You have " + str(5 - num_try) + " try left"
			user_input_answer = raw_input("The answer is wrong, try again: " + " ")
			num_try += 1			
		if check_answer(user_input_answer, answer, index_blank) == 'Correct':
			print("Correct! \n")
			quiz = quiz.replace(white_blanks[index_blank], user_input_answer)
			print quiz + "\n"
			index_blank += 1
	if index_blank == len(white_blanks):
		return congratulation 
	else:
		return sorry

print fill_in_blanks() 



# We've also given you a file called fill-in-the-blanks.pyc which is a working version of the project.
# A .pyc file is a Python file that has been translated into "byte code".
# This means the code will run the same as the original .py file, but when you open it
# it won't look like Python code! But you can run it just like a regular Python file
# to see how your code should behave.

# Hint: It might help to think about how this project relates to the Mad Libs generator you built with Sean.
# In the Mad Libs generator, you take a paragraph and replace all instances of NOUN and VERB.
# How can you adapt that design to work with numbered blanks?

# If you need help, you can sign up for a 1 on 1 coaching appointment: https://calendly.com/ipnd1-1/20min/
