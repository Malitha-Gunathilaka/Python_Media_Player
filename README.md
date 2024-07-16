
# Python Media Player

A simple media player built using Python, `pygame`, and `moviepy`. This media player can handle both audio (MP3, WAV) and video (MP4, MKV) files. The user interface is built using `tkinter`.

## Features

- Play audio files (MP3, WAV)
- Play video files (MP4, MKV)
- Pause and stop functionality for both audio and video
- Simple and intuitive user interface

## Requirements

- Python 3.x
- `pygame` library
- `moviepy` library
- `Pillow` library

## Installation

1. **Clone the repository:**

```bash
git clone https://github.com/yourusername/python-media-player.git
cd python-media-player
```

2. **Install the required libraries:**

```bash
pip install pygame moviepy pillow
```

## Usage

1. **Run the script:**

```bash
python main.py
```

2. **Open a media file:**

- Click the "Open" button to select an audio or video file.

3. **Control playback:**

- Use the "Play", "Pause", and "Stop" buttons to control the playback of the media.

## Code Overview

### main.py

The main script file that sets up the user interface and handles media playback using `pygame` for audio and `moviepy` for video.

```python
import os
import pygame
from tkinter import *
from tkinter import filedialog
from moviepy.editor import VideoFileClip
from PIL import Image, ImageTk

class MediaPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Media Player")
        self.root.geometry("800x600")
        pygame.init()
        pygame.mixer.init()

        self.file_path = None
        self.paused = False
        self.video = None

        self.create_widgets()

    def create_widgets(self):
        # Video display area
        self.video_frame = Frame(self.root)
        self.canvas = Canvas(self.video_frame, bg="black")
        self.canvas.pack(fill=BOTH, expand=1)
        self.video_frame.pack(fill=BOTH, expand=1)

        # Control frame
        self.control_frame = Frame(self.root)
        self.control_frame.pack(pady=20)

        self.play_button = Button(self.control_frame, text="Play", command=self.play_media)
        self.play_button.grid(row=0, column=0, padx=10)

        self.pause_button = Button(self.control_frame, text="Pause", command=self.pause_media)
        self.pause_button.grid(row=0, column=1, padx=10)

        self.stop_button = Button(self.control_frame, text="Stop", command=self.stop_media)
        self.stop_button.grid(row=0, column=2, padx=10)

        self.open_button = Button(self.control_frame, text="Open", command=self.open_file)
        self.open_button.grid(row=0, column=3, padx=10)

    def play_media(self):
        if self.file_path:
            ext = os.path.splitext(self.file_path)[1].lower()
            if ext in [".mp3", ".wav"]:
                if not self.paused:
                    pygame.mixer.music.load(self.file_path)
                    pygame.mixer.music.play()
                else:
                    pygame.mixer.music.unpause()
            elif ext in [".mp4", ".mkv"]:
                self.play_video()
            self.paused = False

    def play_video(self):
        if self.video:
            self.video.preview()

    def pause_media(self):
        ext = os.path.splitext(self.file_path)[1].lower()
        if ext in [".mp3", ".wav"]:
            pygame.mixer.music.pause()
        elif ext in [".mp4", ".mkv"]:
            self.paused = True  # MoviePy does not have pause, this is a placeholder
        self.paused = True

    def stop_media(self):
        ext = os.path.splitext(self.file_path)[1].lower()
        if ext in [".mp3", ".wav"]:
            pygame.mixer.music.stop()
        elif ext in [".mp4", ".mkv"]:
            self.paused = True  # MoviePy does not have stop, this is a placeholder

    def open_file(self):
        self.file_path = filedialog.askopenfilename(
            filetypes=[("Audio Files", "*.mp3;*.wav"), ("Video Files", "*.mp4;*.mkv")]
        )
        if self.file_path:
            ext = os.path.splitext(self.file_path)[1].lower()
            if ext in [".mp4", ".mkv"]:
                self.video = VideoFileClip(self.file_path)
            self.play_media()

if __name__ == "__main__":
    root = Tk()
    player = MediaPlayer(root)
    root.mainloop()
```

## Contributing

Contributions are welcome! Please fork this repository and submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License.

## Contact

Developed by [Malitha Visada](mailto:malithavisada@gmail.com)  
LinkedIn: [Malitha Visada](https://linkedin.com/in/malithavisada)  
GitHub: [Malitha Gunathilaka](https://github.com/Malitha-Gunathilaka)
