import win32gui, win32com.client
import pyautogui
import time
import json
import socket
# pyautogui.hotkey('Alt', 'q') # Press the Ctrl-C hotkey combination.


import discord
import os
from dotenv import load_dotenv
import re

from win10toast import ToastNotifier

import downloadImage
from downloadImage import downloadImageFile, get15SecondFile

from findActiveWindow import findDiscordWindow, raise_window

### COMMAND
# $switchoff/$switchon
SWITCH_BOOLEAN = False

import winsound

def make_some_noise():
	frequency = 2500  # Set Frequency To 2500 Hertz
	duration = 2000  # Set Duration To 1000 ms == 1 second
	winsound.Beep(frequency, duration)

# Loading dataset from csv file
dir_path = os.path.dirname(os.path.realpath(__file__))
load_dotenv()
client = discord.Client()
toaster = ToastNotifier()

### THIS ONE IS FOR TESTING TOASTER
toaster.show_toast(
		"TEST",
		"Working normally",
		duration=2
	)

### THIS ONE IS FOR TESTING SOUND WARNING
make_some_noise()

def show_noti_epic_guard():
	toaster.show_toast(
		"EPIC GUARD",
		"Cảnh sát check",
		duration=3
	)

Bao_id = 419041968094445568
Thao_user = 'whyimpro#9865'

array_name = ["405714559857590283","883408687429980260"]
HOST = '192.168.0.105'  # The server's hostname or IP address
PORT = 8999        # The port used by the server

image_folder = 'images'


icon_pattern = ':\w+:'
# bold_pattern = '\*\*\w+\*\*' # Old one doesn work with space maybe remove in future
bold_pattern = '\*\*[\w ]+\*\*'
num_of_rubies = None


@client.event
async def on_ready():
	print('I have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
	if message.author == client.user:
		return 

	if message.content.lower().startswith("$switchoff") and (message.author==Thao_user):
		SWITCH_BOOLEAN = False
		await message.channel.send('**SWITCH MODE: OFF**')
	if message.content.lower().startswith("$switchon") and (message.author==Thao_user):
		await message.channel.send('**SWITCH MODE: ON**')


	if message.content.startswith('$Hello'):
		await message.channel.send('Mình là Thảo đẹp trai')
		print(message.author)
		await message.channel.send(message.author.mention)
		await message.channel.send(f'You are in the script <@!{Bao_id}>!')
	
	if ("EPIC GUARD" in message.content) and ("stop there" in message.content):
		print(message.author)
		print('Bớ người ta cảnh sát check!')
		print('###################################################')
		print('message.channel\n')
		print(message.channel.name)
		print('message.content\n')
		print(message.content)

		if (message.channel.name == 'thao-channel'): # and ("<!@405714559857590283>" in message.content) :
			make_some_noise()
			raise_window('Discord')
			show_noti_epic_guard()
			# findDiscordWindow()
			
		
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

	# Check if I'm in the jail
	# <@whyimpro>, you are in the jail! type rpg jail
	if ("you are in the **jail**" in message.content) and any([name for name in array_name if name in message.content]):
		print(message.content)
		try:
			with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
				time.sleep(2)
				s.connect((HOST, PORT))
				s.send(b'quit\n')
				data = s.recv(1024).decode
				print('Data received from server:',data) # THIS NEVER HAPPENS!
		except ConnectionRefusedError as err:
			print(err)
			print('Server is not available at the momment!')
		except ConnectionResetError as err:
			print(err)
			print('Server is disconnected and closed!')


client.run(os.getenv('DISCORD_TOKEN'))
