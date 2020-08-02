#!/usr/bin/env python3
# custom_seating_cards.py - From practice project in ch 15, add image to custom card
# Extension of ch 15 project.

import os

from PIL import Image, ImageDraw, ImageFont

def seating_card(guest_list):
    """Custom invitation card for each guest"""
    os.makedirs('custom_cards', exist_ok=True)

    flower_img = Image.open('flower.png')

    with open(guest_list) as f:
        for line in f:
            guest = line[:-1]

            card = Image.new('RGBA', (288, 360), 'white')
            # Paste flower into card image
            card.paste(flower_img, (0,0))

            # Create border
            border = Image.new('RGBA', (291, 363), 'black')
            border.paste(card, (3, 3))

            draw_obj = ImageDraw.Draw(border)
            card_font = ImageFont.truetype('Arial Unicode.ttf', 20)
            draw_obj.text((120, 100), guest, fill='purple', font=card_font)

            border.save(os.path.join('custom_cards', '{}.png'.format(guest)))


if __name__ == "__main__":
    seating_card('guests.txt')
