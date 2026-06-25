from PIL import Image, ImageDraw, ImageFont
import numpy as np
import cv2 as cv
import json

def get_brightness(char):
    img_width = 40
    img_height = 40

    img = Image.new("RGB", (img_width, img_height), (0, 0, 0))

    font = ImageFont.truetype("C:/Windows/Fonts/msgothic.ttc", size=40)
    d = ImageDraw.Draw(img)

    d.text(
        xy=(0, 0), 
        text=char,
        font=font,
        fill=(255, 255, 255)
    )

    img_rgb = np.array(img)
    img_bgr = cv.cvtColor(img_rgb, cv.COLOR_RGB2BGR)

    brightnesses = []
    for i in range(2):
        for j in range(2):
            start_y = i * 20
            start_x = j * 20
            quadrant_blue = img_bgr[start_y:start_y + 20, start_x:start_x + 20, 0]
            brightnesses.append(np.mean(quadrant_blue) / 255)

    return brightnesses


filter = [" ", "\n", "　", "？", "「", "」", "！"]

with open("assets/lyrics.txt", "r", encoding="utf-8") as f:
    lyrics = f.read()
    chars = list(set(lyrics))

for filtered_char in filter:
    if filtered_char in chars:
        chars.remove(filtered_char)

brightness_dict = {}
brightest = 0
dimmest = 1

for char in chars:
    current = get_brightness(char)
    brightness_dict[char] = current

    brightest_quadrant = max(current)
    if brightest_quadrant > brightest:
        brightest = brightest_quadrant

    dimmest_quadrant = min(current)
    if dimmest_quadrant < dimmest:
        dimmest = dimmest_quadrant

for key in brightness_dict:
    value = brightness_dict[key].copy()
    brightness_dict[key] = list(map(lambda x: (x - dimmest) / (brightest - dimmest), value))

json_str = json.dumps(brightness_dict, indent=4)

with open("brightnesses.json", "w") as f:
    f.write(json_str)