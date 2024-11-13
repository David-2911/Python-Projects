from gtts import gTTS  # type: ignore
import os
from tkinter import Tk, Canvas, Entry, Button
import platform
import subprocess


def play_audio(file):
    if platform.system() == "Darwin":
        subprocess.call(["afplay", file])
    elif platform.system() == "Windows":
        os.system(f"start {file}")
    else:
        subprocess.call(["mpg123", file])


def textToSpeech():
    text = entry.get()
    language = "en"
    output = gTTS(text=text, lang=language, slow=False)
    output.save("output.mp3")
    play_audio("output.mp3")


root = Tk()
canvas = Canvas(root, width=400, height=400)
canvas.pack()

entry = Entry(root)
canvas.create_window(200, 180, window=entry)

button = Button(text="Start", command=textToSpeech)
canvas.create_window(200, 230, window=button)

root.mainloop()
