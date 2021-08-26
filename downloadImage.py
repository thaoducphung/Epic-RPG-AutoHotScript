import requests
from tqdm import tqdm
import os
from glob import glob
import time
import datetime
import shutil

STRING_ARRAY = """fish
banana
epic fish
unicorn horn
mermaid hair
apple
life potion
golden fish
zombie eye
epic coin
coin
ruby
wolf skin
chip""".split("\n")

# string_array = STRING_ARRAY.split("\n")
# print('string_array',STRING_ARRAY)

def downloadImageFile(dir_path,image_folder,user_name,image_url):
	filename = user_name+ '_' +image_url.split("/")[-3] + '_' + image_url.split("/")[-2] + '.png'
	filename = os.path.join(dir_path,image_folder,filename)
	# Streaming, so we can iterate over the response.
	response = requests.get(image_url, stream=True)
	total_size_in_bytes= int(response.headers.get('content-length', 0))
	block_size = 1024 #1 Kibibyte
	progress_bar = tqdm(total=total_size_in_bytes, unit='iB', unit_scale=True)
	with open(filename,'wb') as file:
	    for data in response.iter_content(block_size):
	        progress_bar.update(len(data))
	        file.write(data)
	progress_bar.close()
	if total_size_in_bytes != 0 and progress_bar.n != total_size_in_bytes:
	    print("ERROR, something went wrong! Cannot download image file!")

def get15SecondFile(dir_path,image_folder,message_author,folder_name,extension='*.png'):
	for filename in glob(os.path.join(dir_path,image_folder, extension)):
		print('filename:',filename)
		name_image = filename.split("\\")[-1]
		author_name = name_image.split('_')[0]

		date_modified = datetime.datetime.fromtimestamp(os.path.getmtime(filename))
		elapsed = datetime.datetime.now() - date_modified
		if elapsed < datetime.timedelta(seconds=15):
			print("PASS 15 seconds")
			# Check if author is the one creating image
			if author_name == message_author:
				folder_dir = os.path.join(dir_path,image_folder, folder_name)
				if not os.path.exists(folder_dir): # Check if folder exists else create one!
					os.mkdir(folder_dir)
				destination = os.path.join(folder_dir,name_image)
				# print('destination',destination)
				shutil.move(filename, destination)
				print('Moved:', name_image, ' to folder ', folder_name)
			# Move to folder based on author answer
		else: # If later than 15 seconds, then move it into UnlabeledImage
			folder_dir = os.path.join(dir_path, image_folder, 'UnlabeledImage')
			# print('folder_dir',folder_dir)
			print('name_image',name_image)
			destination = os.path.join(folder_dir,name_image)
			# print('destination',destination)
			shutil.move(filename, destination)
			print('Moved:', name_image, ' to folder UnlabeledImage')

if __name__ == '__main__':
	import shutil # to save it locally

	# Loading dataset from csv file
	dir_path = os.path.dirname(os.path.realpath(__file__))

	image_folder = 'images'
	user_name = 'whyimpro#9865'
	## Set up the image URL and filename
	image_url = "https://cdn.discordapp.com/attachments/877222360544055416/880197535833129021/epic_guard.png"
	filename = image_url.split("/")[-3] + '_' + image_url.split("/")[-2] + '.png'
	filename = os.path.join(dir_path,image_folder,filename)
	print(filename)

	# # Open the url image, set stream to True, this will return the stream content.
	# r = requests.get(image_url, stream = True)

	# # Check if the image was retrieved successfully
	# if r.status_code == 200:
	#     # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
	#     r.raw.decode_content = True
	    
	#     # Open a local file with wb ( write binary ) permission.
	#     with open(filename,'wb') as f:
	#         shutil.copyfileobj(r.raw, f)
	        
	#     print('Image sucessfully Downloaded: ',filename)
	# else:
	#     print('Image Couldn\'t be retreived')

	downloadImage(dir_path,image_folder,user_name,image_url)

	# message_author = str(message.author)
	message_author = user_name
	# folder_name = message.content.strip().lower()
	folder_name = 'Testing'
	get15SecondFile(dir_path,image_folder,message_author,folder_name)