#!/usr/bin/env python3
# image_downloader - Downloads images from Imgur

import requests, os, bs4
import pyinputplus as pyip

pic_count = 0
search = input('What would you like to search for?\n')
num_pics = pyip.inputInt('How many pictures would you like downloaded?\n')
url = 'https://imgur.com/search?q=' + search    # starting url
os.makedirs('imgur', exist_ok=True)      # store comics in ./imgur
while pic_count < num_pics:
    # Download the page.
    print(f'Downloading page {url}...')
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    # Find the URL of image.
    img_elem = soup.select('.post > .image-list-link img')

    for count, image in enumerate(img_elem):
        if img_elem == []:
            print('Could not find comic image')
        else:
            img_url = 'https:' + img_elem[count].get('src')
            # Download the image.
            print(f'Downloading the image {img_url}')
            res = requests.get(img_url)
            res.raise_for_status()

            # Save the image to ./imgur.
            image_file = open(os.path.join('imgur', os.path.basename(img_url)), 'wb')
            for chunk in res.iter_content(100000):
                image_file.write(chunk)
            image_file.close()

            pic_count += 1
            if pic_count >= num_pics:
                break

print('Done.')

    