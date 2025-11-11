import os
import time
from text_to_audio import text_to_speech_file
import subprocess

def text_to_audio(folder):
    with open(f"user_uploads/{folder}/desc.txt") as f:
        text = f.read()
    text_to_speech_file(text, folder)

def create_reel(folder):
    command=f'''ffmpeg -f concat -safe 0 -i user_uploads/{folder}/input.txt -i user_uploads/{folder}/audio.mp3 -vf "scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2:black" -c:v libx264 -c:a aac -shortest -r 30 -pix_fmt yuv420p static/reels/{folder}.mp4'''
    subprocess.run(command, shell=True,check=True)
    print(folder)

if __name__ == "__main__":
    while True:
        # Read already processed folders
        with open("done.txt", "r") as f:
            done_folders = f.readlines()
        done_folders = [x.strip() for x in done_folders]
        
        # Get only actual directories, excluding hidden files like .DS_Store
        folders = []
        for item in os.listdir("user_uploads"):
            item_path = os.path.join("user_uploads", item)
            if os.path.isdir(item_path) and not item.startswith('.'):
                folders.append(item)
        
        # Process each folder
        for folder in folders:
            if folder not in done_folders:
                try:
                    text_to_audio(folder)
                    create_reel(folder)
                    with open("done.txt", "a") as f:
                        f.write(folder + "\n")
                except Exception as e:
                    print(f"Error processing folder {folder}: {e}")
        
        time.sleep(5)
