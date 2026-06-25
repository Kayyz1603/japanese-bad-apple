About
=
A terminal-based player for the music video "Bad Apple!!", but rendered with only Japanese characters found in its lyrics, made in Python. This project explores concepts similar to anti-aliasing and sub-pixel rendering, in the context of being limited to printing characters in a terminal.

[Watch the YouTube video!](https://youtu.be/HK2-K6gNbNU)

Technical Design and Challenges
=
- **Anti-aliasing and sub-character rendering:** The program achieves a smoother look in the final video by splitting each Japanese character into 4 regions and computing the average brightness in each. This data is then used to find the character that best matches the brightness and shape of a given region of the video, thereby implementing a similar technology to anti-aliasing and sub-pixel rendering.
- **Render optimization:** To avoid long run times when generating all 3287 frames, pixel regions that are detected to be purely black or white are immediately assigned predetermined characters which are the closest to fully black or white.
- **Effectiveness of sub-character rendering:** In the final video, the technique used doesn't seem to have a big impact, due to most Japanese characters having a similar density of strokes in the entire character. This is practical from a font design standpoint, but doesn't create the best result when the video is full of edges going from fully black to fully white.

Quick Setup (to play the video only)
=
**1. Clone repository**\
Use `git clone https://github.com/Kayyz1603/japanese-bad-apple.git` to clone the repository from GitHub.\
**2. Run player**\
Navigate into the root folder with `cd japanese-bad-apple` then run the player with `python player.py`.

Additional Setup (to generate the video from scratch)
=
**3. Create virtual environment**\
Run `python -m venv .venv` then `.venv\Scripts\activate` to create and activate a virtual environment.\
**4. Install dependencies**\
Install the required libraries listed in `requirements.txt` with `pip install -r requirements.txt`.\
**5. Get the Bad Apple video frames**\
Download an mp4 file of the Bad Apple music video from [YouTube](https://www.youtube.com/watch?v=FtutLA63Cp8) at 240p, and extract the frames using ffmpeg, using the command `ffmpeg -i bad_apple.mp4 -vf fps=15 frame_%04d.jpg` (replace `bad_apple.mp4` with your file own name). Make sure to move all the frames into the directory `assets/bad_apple_frames`.\
**6. Generate video**\
Run `python brightness_generator.py` and `python frame_generator.py` to generate required data from the characters and generate and store the frames respectively.
