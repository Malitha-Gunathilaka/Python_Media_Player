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
