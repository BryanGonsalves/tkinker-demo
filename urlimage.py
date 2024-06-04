import tkinter as tk
import urllib.request

from PIL import Image, ImageTk

window=tk.Tk()
window.geometry("400x400")
window.title("My App")

urllib.request.urlretrieve('https://bit.ly/38NswPn',"url_image.png")
  
image = Image.open("url_image.png")

image.thumbnail((200,200),Image.ANTIALIAS)

photo= ImageTk.PhotoImage(image)

label_image= tk.Label(image=photo)
label_image.grid(column=0,row=0)

window.mainloop()