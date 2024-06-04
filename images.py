import tkinter as tk

from PIL import Image, ImageTk

window=tk.Tk()
window.geometry("400x400")
window.title("My App")

image = Image.open('./images/apples.jpg')

image.thumbnail((200,200),Image.ANTIALIAS)

photo= ImageTk.PhotoImage(image)

label_image= tk.Label(image=photo)
label_image.grid(column=0,row=0)

window.mainloop()