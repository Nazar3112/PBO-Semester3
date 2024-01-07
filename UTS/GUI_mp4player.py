import tkinter as tk
from tkinter import filedialog, Button, PhotoImage, messagebox
from moviepy.editor import VideoFileClip
from threading import Thread

class VideoPlayer:
    def __init__(self, master):
        self.master = master
        self.master.title("Video Player")   

        self.video_path = ""
        self.video_clip = None
        self.playing = False

        # UI elements
        image_folder_path = 'C:/Users/nazar/PBO/UTS/Media/iconfolder.png'
        self.folder_button_image = PhotoImage(file=image_folder_path)
        self.select_button = tk.Button(master, image=self.folder_button_image, command=self.select_video)
        self.select_button.pack(pady=10)

        image_play_path = 'C:/Users/nazar/PBO/UTS/Media/iconplay.png'
        self.play_button_image = PhotoImage(file=image_play_path)
        self.play_button = tk.Button(master, image=self.play_button_image, command=self.toggle_play)
        self.play_button.pack(pady=10)

    def select_video(self):
        file_path = filedialog.askopenfilename(title="Pilih File Video", filetypes=[("Video files", "*.mp4;*.avi;*.mkv")])

        if file_path:
            self.video_path = file_path

    def toggle_play(self):
        if not self.video_path:
            messagebox.showwarning("Peringatan", "Pilih file video terlebih dahulu!")
            return

        if not self.playing:
            self.playing = True
            self.play_button.config(image=self.play_button_image, text="Pause")
            self.video_clip = VideoFileClip(self.video_path)
            self.video_thread = Thread(target=self._play_video_thread)
            self.video_thread.start()
        else:
            self.playing = False
            self.play_button.config(image=self.play_button_image, text="Play")

    def _play_video_thread(self):
        self.video_clip.preview()
        self.playing = False
        self.play_button.config(image=self.play_button_image, text="Play")

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("250x150")
    root.resizable(False, False)
    player = VideoPlayer(root)
    root.mainloop()
