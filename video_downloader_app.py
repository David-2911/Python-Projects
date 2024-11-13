from tkinter import Tk, Canvas, Label, Button, Entry, filedialog
from pytube import YouTube  # type: ignore
from moviepy.editor import VideoFileClip  # type: ignore
import shutil


def download_video():
    try:
        url = url_entry.get()
        path = path_label.cget("text")
        yt = YouTube(
            url,
            on_progress_callback=None,
            on_complete_callback=None,
            proxies=None,
            use_oauth=False,
            allow_oauth_cache=True,
        )
        mp4 = yt.streams.get_highest_resolution().download(path)
        video_clip = VideoFileClip(mp4)

        # for mp3
        audio_file = video_clip.audio
        audio_file.write_audiofile(mp4.replace(".mp4", ".mp3"))
        audio_file.close()
        shutil.move(mp4.replace(".mp4", ".mp3"), path)
        # for mp3

        video_clip.close()
        shutil.move(mp4, path)
        result_label.config(text="Video downloaded successfully!")
    except Exception as e:
        result_label.config(text="Error: " + str(e))


def select_path():
    path = filedialog.askdirectory()
    if path:
        path_label.config(text=path)


root = Tk()
root.title("Video Downloader")

canvas = Canvas(root, width=400, height=400)
canvas.pack()

app_label = Label(root, text="Video Downloader", font=("Helvetica", 16))
canvas.create_window(200, 50, window=app_label)

url_label = Label(root, text="Enter video URL here", font=("Helvetica", 12))
canvas.create_window(200, 100, window=url_label)

url_entry = Entry(root)
canvas.create_window(200, 130, window=url_entry)

path_label = Label(root, text="Select path to save video", font=("Helvetica", 12))
canvas.create_window(200, 160, window=path_label)

path_button = Button(root, text="Select Path", command=select_path)
canvas.create_window(200, 190, window=path_button)

download_button = Button(root, text="Download Video", command=download_video)
canvas.create_window(200, 270, window=download_button)

result_label = Label(root, text="")
canvas.create_window(200, 320, window=result_label)

root.mainloop()
