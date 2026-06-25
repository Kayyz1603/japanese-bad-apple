import cv2 as cv
import numpy as np
import json

frame_width = 32
frame_height = 24
frame_amount = 3287

with open("brightnesses.json", "r", encoding="utf-8") as f:
    data = json.load(f)

export_file = open("frames.txt", "w", encoding="utf-8")

char_matrix = np.array([data[key] for key in data.keys()])
char_list = list(data.keys())

for frame_number in range(1, frame_amount + 1):
    img = cv.imread(f"assets/bad_apple_frames/frame_{frame_number:04}.jpg")

    if img is None:
        print(f"Could not find frame_{frame_number:04}.jpg")

    quadrant_length = int(120 / frame_height)
    block_length = int(240 / frame_height)

    current_frame = ""

    for i in range(frame_height):
        start_y = i * block_length

        for j in range(frame_width):
            start_x = j * block_length

            block_blue = img[start_y:start_y + block_length, start_x:start_x + block_length, 0]

            block_blue_normalized = block_blue / 255

            top_left = np.mean(block_blue_normalized[0:quadrant_length, 0:quadrant_length])
            top_right = np.mean(block_blue_normalized[0:quadrant_length, quadrant_length:quadrant_length * 2])
            bottom_left = np.mean(block_blue_normalized[quadrant_length:quadrant_length * 2, 0:quadrant_length])
            bottom_right = np.mean(block_blue_normalized[quadrant_length:quadrant_length * 2, quadrant_length:quadrant_length * 2])
            
            frame_block = np.array([top_left, top_right, bottom_left, bottom_right])

            if np.sum(frame_block) > 3.99:
                current_frame += "開"
            elif np.sum(frame_block) < 0.01:
                current_frame += "く"
            else:
                costs = np.sum((char_matrix - frame_block) ** 2, axis=1)

                best_char_index = np.argmin(costs)
                current_frame += char_list[best_char_index]

        current_frame += "\n"

    export_file.write(current_frame + "END\n")

export_file.close()