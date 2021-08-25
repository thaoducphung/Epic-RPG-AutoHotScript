# import pyautogui

# pyautogui.hotkey('Alt', 'q') # Press the Ctrl-C hotkey combination.


import discord
import os
from dotenv import load_dotenv
import re

load_dotenv()
Bao_id = 419041968094445568
client = discord.Client()

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

icon_pattern = ':\w+:'
bold_pattern = '\*\*\w+\*\*'


num_of_rubies = None

# Loading dataset from csv file
dir_path = os.path.dirname(os.path.realpath(__file__))

@client.event
async def on_ready():
	print('I have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
	if message.author == client.user:
		return

	# # if (message.channel.name != 'thao-channel') and (message.channel.name != 'bao-channel'):
	# if (message.channel.name != 'thao-channel'):
	# 	if message.content.startswith('$hello'):
	# 		await message.channel.send(f'Mình là Bảo cùi <@!{Bao_id}> !')
	# 	return

	if message.content.startswith('$hello'):
		await message.channel.send('Mình là Thảo đẹp trai')
		await message.channel.send(message.author.mention)
		await message.channel.send(f'You are in the script <@!{Bao_id}>!')
	
	if ("EPIC GUARD" in message.content) and ("stop there" in message.content):
		print('Bớ người ta cảnh sát check!')
		print('###################################################')
		print(message.channel.name)
		print(message.content)
		print('###################################################')
		await message.channel.send('Bớ người ta cảnh sát check!')

	# print(message)
	# print(message.author)
	# print(message.author.mention)

	# if (message.channel.name == 'thao-channel'):


		# print(message.content)
		# embeds = message.embeds # return list of embeds
		# if not embeds:
		# 	print('Embedded is NONE!')
		# 	# print(type(embeds))
		# else:
		# 	print('EMBEDDED:\n')
		# 	for embed in embeds:
		# 		print(embed.to_dict()) # it's content of embed in dict
		# 	print('END!\n')


	if '**NOPE!**' in message.content:
		rubies_question = re.search(r'\d', s)
		rubies_question = rubies_question.group(0)

	if 'is training' in message.content:
		with open(os.path.join(dir_path,'training.txt'),'a') as fd:
			fd.write(message.content+'\n')
		question_raw = message.content
		question = question_raw.lower().split('\n')[1]
		if "name of" in question:
			find_word = re.search(icon_pattern,question)
			key_word = find_word.group(0).replace(':','')
			key_word = key_word.lower()
			if 'normie' in key_word:
				await message.channel.send('1')
			elif 'golden' in key_word:
				await message.channel.send('2')
			elif 'epic' in key_word:
				await message.channel.send('3')
		elif "letter of" in question:
			find_bold_word = re.search(bold_pattern,question)
			find_key_word = re.search(icon_pattern,question)
			
			bold_word = find_bold_word.group(0).replace('*','')
			bold_word = bold_word.lower()

			key_word = find_key_word.group(0).replace(':','')
			key_word = key_word.lower()

			print(key_word[mapping_letter[bold_word]-1])
			await message.channel.send(key_word[mapping_letter[bold_word]-1])

		elif "is this" in question:
			find_bold_word = re.search(bold_pattern,question)
			find_key_word = re.search(icon_pattern,question)
			
			bold_word = find_bold_word.group(0).replace('*','')
			bold_word = bold_word.lower()

			key_word = find_key_word.group(0).replace(':','')
			key_word = key_word.lower()

			if mapping_icon[bold_word] == key_word:
				await message.channel.send('Y')
			else:
				await message.channel.send('N')
		elif "rubies" in question:
			if num_of_rubies is None:
				await message.channel.send("Not implement yet! Take a guess!")
			else:
				await message.channel.send(str(num_of_rubies))
		else:
			log_icon = question_raw.lower().split('\n')[-1]
			find_icon_pattern = re.search(icon_pattern,log_icon)
			log_key_word = find_icon_pattern.group(0)
			log_number = len(re.findall(log_key_word, question))
			await message.channel.send(log_number)


client.run(os.getenv('DISCORD_TOKEN'))


# banana

## Check if the author mention TRAINING
# Then capture the next question
# Write then into csv
# Save history and analyze it