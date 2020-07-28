#!/usr/bin/env python3
# scheduled_comic_downloader.py - Checks if latest web comics of qwantz and xkcd are downloaded.

import bs4, datetime, os, requests

# Creates directory to play in.
folder_name = 'web-comics'
os.makedirs(folder_name, exist_ok=True)

# Downloads comic image if not found already in directory.
def check_comic(comic_url):

	# Get image filename.
	file_name = os.path.basename(comic_url)
	
	# Check if today's comic exists in directory.
	if file_name in os.listdir(folder_name):
		print(f'Most recent comic is already downloaded {comic_url}.')
	
	# Else download today's comic.
	else:
		print(f'Downloading {comic_url}...')

		res = requests.get(comic_url)
		res.raise_for_status()
		image_file = open(os.path.join(folder_name, file_name), 'wb')
		for chunk in res.iter_content(100000):
			image_file.write(chunk)
		image_file.close()

def get_qwantz_comic():

	# Get today's comic's url.
	base_url = 'http://www.qwantz.com'
	
	# Get url text to parse for img.
	res = requests.get(base_url)
	res.raise_for_status()
	soup = bs4.BeautifulSoup(res.text, 'html.parser')
	
	# Get image url.
	comic_elem = soup.select('.comic')
	comic_url_short = comic_elem[0].get('src')
	comic_url = base_url + '/' + comic_url_short
	
	# Confirm whether there is an img url.
	if comic_elem == 0:
		print(f'Could not find comic element at {base_url}.')

	# Begin download of img with url.
	else:
		check_comic(comic_url)

	
def get_xkcd_comic():

	# Get today's comic's url.	
	base_url = 'https://xkcd.com'
	
	# Get url text to parse for img.
	res = requests.get(base_url)
	res.raise_for_status()
	soup = bs4.BeautifulSoup(res.text, 'html.parser')
	
	# Get image url.
	comic_elem = soup.select('#comic > img')
	comic_url_short = comic_elem[0].get('src')
	comic_url = 'http:' + comic_url_short
	
	# Confirm whether there is an img url.
	if comic_elem == 0:
		print(f'Could not find comic element at {base_url}.')

	# Begin download of img with url.
	else:
		check_comic(comic_url)

with open('web-comics/last_downloaded.txt', 'r') as f:
    print(f.read())

get_qwantz_comic()
get_xkcd_comic()

date = datetime.datetime.now().strftime('%H:%M:%S on %m/%d/%Y')
print('Current date: ', date)

with open('web-comics/last_downloaded.txt', 'w') as f:
    f.write('Last batch of comic downloaded at: ' + date + '\n')

print('Done!')



