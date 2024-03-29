#! python3
# random quiz generator
# random order, along with the answer key
# Running this file creates 70.txt files in total. 35 for questions, 35 for answers

import random

# Quiz data

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix', 'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver', 'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee', 'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois': 'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine': 'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan': 'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri': 'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada': 'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City', 'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence', 'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee': 'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont': 'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

# generate 35 quiz files

for quizNum in range(35):

	# create the quiz and answer key files
	quizFile = open(f'capitalsquiz{quizNum + 1}.txt', 'w')
	answerKeyFile = open(f'capitalsquiz_answers{quizNum + 1}.txt', 'w')

	# write out the header for the quiz
	quizFile.write('Name:\n\nDate:\n\n')
	quizFile.write((' ' * 20) + f'State capitals quiz (Form {quizNum + 1})')
	quizFile.write('\n\n')

	# shuffle the order of the states
	states = list(capitals.keys())
	random.shuffle(states)

	# loop through all 50 states, making a question for each
	for questionNum in range(50):

		# get right and wrong answers
		correctAnswer = capitals[states[questionNum]]
		wrongAnswers = list(capitals.values())
		del wrongAnswers[wrongAnswers.index(correctAnswer)]
		wrongAnswers = random.sample(wrongAnswers, 3)
		answerOptions = wrongAnswers + [correctAnswer]
		random.shuffle(answerOptions)

		# write the question and answer options to the quiz file
		quizFile.write(f'{questionNum + 1}. What is the capital of {states[questionNum]}?\n')
		for i in range(4):
			quizFile.write(f"	{'ABCD'[i]}.{ answerOptions[i]}\n")
		quizFile.write('\n')

		# Write the answer key to the file
		answerKeyFile.write(f"{questionNum + 1}. {'ABCD'[answerOptions.index(correctAnswer)]}\n")
	quizFile.close()
	answerKeyFile.close()