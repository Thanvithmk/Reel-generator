AI Reel Generator: Image and Text to Video Reel
This project is a Flask-based web application designed to automatically generate short-form video reels (e.g., for Instagram or TikTok) by combining a sequence of user-uploaded images with a generated voice-over and background music.

🎯 The Core Functionality
The AI Reel Generator transforms user input into a final video through a two-phase process:

1. User Input & File Preparation (Flask App)
When a user submits images and text via the /create web form:

A unique folder is created in user_uploads/ to store the request's assets.

Uploaded images are saved to this folder.

The user's text script is saved as desc.txt.

A file list, input.txt, is created, instructing FFmpeg to display each image for 1 second.

2. Automated Reel Generation (Background Worker)
A separate background Python script (generate_process.py) continuously monitors the user_uploads folder and executes the following steps for new requests:

Text-to-Speech: The text from desc.txt is converted into a high-quality voice-over using the ElevenLabs API. This audio is saved as audio.mp3.

Video Assembly (FFmpeg): The create_reel function runs an FFmpeg command to produce the final video:

It stitches the images based on the timings in input.txt.

It scales and pads the video to the standard vertical 1080x1920 reel format.

It mixes the voice-over (audio.mp3) with a background music track (static/songs/1.mp3), ensuring the voice-over is distinct over the background audio.

Final Output: The resulting reel is saved as a ready-to-use MP4 file in the static/reels/ directory.

🔑 Key Technologies
Flask (main.py): Hosts the user-facing web application.

ElevenLabs API (text_to_audio.py): Used for high-quality Text-to-Speech voice generation.

FFmpeg (generate_process.py): Handles the heavy-lifting of image-to-video stitching, scaling, and audio mixing.

Dual-Process Model: Uses a separate worker (generate_process.py) to keep the web application responsive while video generation runs in the background.
