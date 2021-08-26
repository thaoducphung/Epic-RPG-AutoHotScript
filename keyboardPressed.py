import pyautogui

# pyautogui.hotkey('Alt', 'q') # Press the Ctrl-C hotkey combination.


import discord
import os
from dotenv import load_dotenv
import re

from win10toast import ToastNotifier

import downloadImage
from downloadImage import downloadImageFile, get15SecondFile

from findActiveWindow import findDiscordWindow



def show_noti_epic_guard():
	toaster.show_toast(
		"EPIC GUARD",
		"Cảnh sát check",
		duration=2
	)

# Loading dataset from csv file
dir_path = os.path.dirname(os.path.realpath(__file__))
load_dotenv()
client = discord.Client()
toaster = ToastNotifier()

Bao_id = 419041968094445568

image_folder = 'images'
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
		print(message.author)
		await message.channel.send(message.author.mention)
		await message.channel.send(f'You are in the script <@!{Bao_id}>!')
	
	if ("EPIC GUARD" in message.content) and ("stop there" in message.content):
		if (message.channel.name == 'thao-channel'):
			show_noti_epic_guard()
			findDiscordWindow()
		print('Bớ người ta cảnh sát check!')
		print('###################################################')
		print('message.channel\n')
		print(message.channel.name)
		print('message.content\n')
		print(message.content)
		# print('message.attachments\n',message.attachments)
		# print(message.attachments)
		# print(message.attachments[0].url)
		try: # When test it - don't have the image, so bypass the error
			image_url = message.attachments[0].url
			user_id = re.search('\d+',message.content)
			user_id = user_id.group(0)
			downloadImageFile(dir_path,image_folder,user_id,image_url)
		except IndexError:
			print('There is no image in the message content!')

		print('###################################################')
		await message.channel.send('Bớ người ta cảnh sát check!')
	# print(str(message.author.id))
	if message.content.strip().lower() in downloadImage.STRING_ARRAY:
		message_author = str(message.author.id)
		folder_name = message.content.strip().lower()
		get15SecondFile(dir_path,image_folder,message_author,folder_name)

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
		rubies_number = re.search(r'\d', message.content.split('\n')[0])
		rubies_number = rubies_number.group(0)
		print('rubies_number',rubies_number)
	try:
		result = None
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
					result = '1'
					await message.channel.send('1')
				elif 'golden' in key_word:
					result = '2'
					await message.channel.send('2')
				elif 'epic' in key_word:
					result = '3'
					await message.channel.send('3')
			elif "letter of" in question:
				find_bold_word = re.search(bold_pattern,question)
				find_key_word = re.search(icon_pattern,question)
				
				bold_word = find_bold_word.group(0).replace('*','')
				bold_word = bold_word.lower()

				key_word = find_key_word.group(0).replace(':','')
				key_word = key_word.lower()

				result = key_word[mapping_letter[bold_word]-1]
				await message.channel.send(result)

			elif "is this" in question:
				find_bold_word = re.search(bold_pattern,question)
				find_key_word = re.search(icon_pattern,question)
				
				bold_word = find_bold_word.group(0).replace('*','')
				bold_word = bold_word.lower()

				key_word = find_key_word.group(0).replace(':','')
				key_word = key_word.lower()

				if mapping_icon[bold_word] == key_word:
					result = 'Y'
					await message.channel.send('Y')
				else:
					result = 'N'
					await message.channel.send('N')
			elif "rubies" in question:
				
				result = 'N'

				if num_of_rubies is None:
					await message.channel.send("Not implement yet! Take a guess!")
				else:
					await message.channel.send(str(num_of_rubies))
			else:
				log_icon = question_raw.lower().split('\n')[-1]
				find_icon_pattern = re.search(icon_pattern,log_icon)
				log_key_word = find_icon_pattern.group(0)
				log_number = len(re.findall(log_key_word, question))
				result = log_number
				await message.channel.send(log_number)

			# Check if user name is whyimpro
			if "**whyimpro**" in question_raw:
				findDiscordWindow()
				pyautogui.press('Enter') # Enter all the current text then type result
				pyautogui.write(str(result)) # prints out result instantly
				pyautogui.press('Enter') # Enter the result

	except Exception as err:
		print(err)
		print(message.content)
		await message.channel.send("SOMETHING'S WRONG! PLEASE CALL THAO!")


client.run(os.getenv('DISCORD_TOKEN'))


# banana

## Check if the author mention TRAINING
# Then capture the next question
# Write then into csv
# Save history and analyze it