import tkinter as tk
import pyqrcode
from PIL import Image, ImageTk


def generate_qrcode():
    link_name = name_entry.get()
    link = link_entry.get()
    qr = pyqrcode.create(link)
    qr.png(link_name + ".png", scale=8)
    image = Image.open(link_name + ".png")
    photo = ImageTk.PhotoImage(image)
    qr_label = tk.Label(image=photo)
    qr_label.image = photo
    canvas.create_window(200, 300, window=qr_label)
    output.config(text="QR Code generated successfully!")


root = tk.Tk()
root.title("QR Code Generator")

canvas = tk.Canvas(root, width=400, height=700)
canvas.pack()

title = tk.Label(root, text="QR Code Generator", font=("Helvetica", 16))
canvas.create_window(200, 50, window=title)

name_label = tk.Label(root, text="Enter link name", font=("Helvetica", 12))
canvas.create_window(200, 100, window=name_label)

link_label = tk.Label(
    root, text="Enter link/data to generate QR Code", font=("Helvetica", 12)
)
canvas.create_window(200, 150, window=link_label)

name_entry = tk.Entry(root)
canvas.create_window(200, 130, window=name_entry)

link_entry = tk.Entry(root)
canvas.create_window(200, 180, window=link_entry)

button = tk.Button(root, text="Generate QR Code", command=generate_qrcode)
canvas.create_window(200, 220, window=button)

output = tk.Label(root, text="")
output.pack(pady=10)

root.mainloop()
