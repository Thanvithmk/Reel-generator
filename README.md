# 📸 AI Reel Generator: Image and Text to Video Reel

This project is a Flask-based web application designed to **automatically generate short-form video reels** (e.g., for Instagram or TikTok) by combining a sequence of user-uploaded images and a text script into a single, vertically formatted video with a **mixed audio track**.

***

## ⚙️ Core Functionality: Image and Text Input

The system operates using a **dual-process architecture** to keep the web application responsive while resource-intensive video processing runs in the background.

### 1. User Input & File Preparation (Flask App)

The Flask application (`main.py`) handles all initial file ingestion and structuring when a user submits the creation form:

* **File Storage:** A unique folder is created in `user_uploads/` for each request.
* **Input Saving:** Uploaded images and the user's text script (`desc.txt`) are saved into this folder.
* **Video Timing:** A file list (`input.txt`) is generated, instructing FFmpeg to display each image for **1 second**.

### 2. Automated Reel Generation (Background Worker)

A separate Python script (`generate_process.py`) runs continuously, monitoring for new requests and executing the video creation workflow:

* **Voice-over Generation:** The text from `desc.txt` is converted into a voice-over audio file (`audio.mp3`) using the **ElevenLabs API**.
* **Video Assembly (FFmpeg):** The `create_reel` function runs a powerful FFmpeg command to produce the final MP4:
    * **Video Formatting:** It stitches the images and formats the video to the vertical **1080x1920** aspect ratio suitable for social media reels.
    * **Audio Mixing:** It combines the voice-over (`audio.mp3`) with a background music track (`static/songs/1.mp3`). The voice-over is set to full volume, and the music is mixed in at a lower volume (`volume=0.3`) to ensure the spoken words are clear.
* **Final Output:** The completed reel is saved as an MP4 file in the `static/reels/` directory.

***

## 🛠️ Key Technologies

| Component | Technology | File/Details | Role |
| :--- | :--- | :--- | :--- |
| **Web App** | **Flask** | `main.py` | Hosts the web interface and handles file uploads. |
| **Worker Process** | **Python** | `generate_process.py` | Executes background tasks and manages the video pipeline. |
| **Text-to-Audio** | **ElevenLabs API** | `text_to_audio.py`, `config.py` | Generates the high-quality voice-over from the user's text. |
| **Video Processing** | **FFmpeg** | `generate_process.py` | Handles image stitching, video scaling, and multi-track audio mixing. |

***

## 🚀 Setup and Running

1.  **Install FFmpeg:** Ensure the `ffmpeg` command-line tool is installed and accessible globally.
2.  **Configure API Key:** Set your ElevenLabs API key in `config.py`.
3.  **Start Processes:** Run the Flask server and the background worker concurrently:
    ```bash
    python main.py
    python generate_process.py
    ```
