import tkinter as tk

window=tk.Tk()
window.title(" My Window ")
window.geometry("600x400")

myCanvas = tk.Canvas(window, bg="lightblue",
           height=300, width=300)
myCanvas.grid(row=0,column=0)

window.mainloop()
