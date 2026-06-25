import time

FRAME_BUDGET = 1 / 15
frame_amount = 30
frame_height = 24

with open("frames.txt", "r", encoding="utf-8") as f:
    loop_start = time.perf_counter()

    current_frame = ""
    frame_number = 1

    for line in f:
        if line.strip() == "END":
            print(current_frame)

            now = time.perf_counter()
            start_next_frame = loop_start + frame_number * FRAME_BUDGET
            sleep_time = start_next_frame - now

            if sleep_time > 0:
                time.sleep(sleep_time)
            else:
                print("[Warning] BUDGET EXCEEDED!")

            current_frame = ""
            frame_number += 1
        else:
            current_frame += line