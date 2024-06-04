import tkinter as tk

window=tk.Tk()
window.title("My Window")
window.geometry("300x300")

frame1 = tk.Frame(window)
frame1.grid(column=0,row=0)

myLabel = tk.Label(frame1,text="Hello World")
myLabel.grid(column=0,row=0)

window.mainloop()