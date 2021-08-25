import os
import re 

# Loading dataset from csv file
dir_path = os.path.dirname(os.path.realpath(__file__))
icon_pattern = ':\w+:'
bold_pattern = '\*\*\w+\*\*'
f = open(os.path.join(dir_path,'training.csv'),"r")
# print(f.read())

mapping_icon = {
	'gift':'gift',
	'coin' :'coin',
	'four leaf clover':'four_leaf_clover',
	'dice':'game_die',
	'diamond':'gem',
}

mapping_letter = {
	'first' : 1,
	'second': 2,
	'third' : 3,
	'fourth': 4,
	'fifth' : 5,
}

letter_questions = ['apple','banana']
message = f.read()


question = message.split('\n')[0]
print('question\n',question)
if '**NOPE!**' in question:
	rubies_question = re.search(r'\d', question)
	rubies_question = rubies_question.group(0)
	print(rubies_question)
os.exit()


question = message.lower().split('\n')[1]
print(question)
if "name of" in question:
	find_word = re.search(icon_pattern,question)
	key_word = find_word.group(0).replace(':','')
	key_word = key_word.lower()
	print(key_word)
	if 'normie' in key_word:
		print(1)
	elif 'golden' in key_word:
		print(2)
	elif 'epic' in key_word:
		print(3)
elif "letter of" in question:
	find_bold_word = re.search(bold_pattern,question)
	find_key_word = re.search(icon_pattern,question)
	
	bold_word = find_bold_word.group(0).replace('*','')
	bold_word = bold_word.lower()

	key_word = find_key_word.group(0).replace(':','')
	key_word = key_word.lower()

	print(key_word[mapping_letter[bold_word]-1])
	# await message.channel.send(key_word[mapping_letter[bold_word]-1])

elif "is this" in question:
	find_bold_word = re.search(bold_pattern,question)
	find_key_word = re.search(icon_pattern,question)
	
	bold_word = find_bold_word.group(0).replace('*','')
	bold_word = bold_word.lower()

	key_word = find_key_word.group(0).replace(':','')
	key_word = key_word.lower()

	if mapping_icon[bold_word] == key_word:
		print('Y')
		# await message.channel.send('Y')
	else:
		print('N')
		# await message.channel.send('N')
else:
	log_icon = message.lower().split('\n')[-1]
	find_icon_pattern = re.search(icon_pattern,log_icon)
	log_key_word = find_icon_pattern.group(0)
	log_number = len(re.findall(log_key_word, question))
	# await message.channel.send(log_number)

f.close()