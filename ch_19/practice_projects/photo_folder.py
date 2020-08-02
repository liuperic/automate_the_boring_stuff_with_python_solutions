#!/usr/bin/env python3
# photo_folder.py - Identifies folders as photo folders based on specified criteria.
# Prints absolute path of photo folders to screen.

import os
from PIL import Image

for foldername, subfolders, filenames, in os.walk('/'):
    num_photo_files = 0
    num_non_photo_files = 0

    for filename in filenames:
        # Check if file extension isn't .png or .jpg
        if not (filename.lower().endswith('.png') or filename.lower().endswith('.jpg')):
            num_non_photo_files += 1
            continue    # Skip to next filename

        # Open image file using Pillow
        photo_im = Image.open(os.path.join(foldername,filename))

        # Check if width & height are larger than 500.
        width, height = photo_im.size

        if width > 500 and height > 500:
            # Image is large enough to be considered a photo.
            num_photo_files += 1
        else:
            # Image is too small to be a photo.
            num_non_photo_files += 1
    
    # If more than half of files were photo.
    # Print the absolute path of the folder.
    if num_photo_files > num_non_photo_files:
        print(os.path.abspath(foldername))
