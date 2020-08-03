#!/usr/bin/env python3
# resize_and_add_logo.py - Resizes all images in current working directory to fit
# in a 300x300 square, and adds catlogo.png to the lower-right corner.

# Extends previous chapter project so code accepts file extensions that are
# case insensitive. Skips adding logo if image is not as least 2x size of logo.

import os
from PIL import Image

SQUARE_FIT_SIZE = 300
LOGO_FILENAME = 'catlogo.png'

# Make sure logo size is small or logo adding will look odd.
logo_im = Image.open(LOGO_FILENAME)
logo_width, logo_height = logo_im.size

os.makedirs('with_logo', exist_ok=True)
# Loop over all files in the working directory.
for filename in os.listdir('.'):
    if not (filename.lower().endswith('.png') or filename.lower().endswith('.jpg')
            or filename.lower().endswith('.gif') or filename.lower().endswith('bmp')) \
            or filename == LOGO_FILENAME:
        continue

    im = Image.open(filename)
    width, height = im.size

    # Check if image needs to be resized.
    if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:
        # Calculate the new width and height to resize to.
        if width > height:
            height = int((SQUARE_FIT_SIZE / width) * height)
            width = SQUARE_FIT_SIZE
        else:
            width = int((SQUARE_FIT_SIZE / height) * width)
            height = SQUARE_FIT_SIZE
        
        # Resize the image.
        print('Resizing %s...' % (filename))
        im = im.resize((width, height))

    # Add logo only if image size is more than 2x logo size.
    if width >= logo_width * 2 and height >= logo_height * 2:
        print('Adding logo to %s...' % (filename))
        im.paste(logo_im, (width - logo_width, height - logo_height), logo_im)
    else:
        print('Logo too big to add to image.')

    # Save changes.
    im.save(os.path.join('with_logo', filename))
