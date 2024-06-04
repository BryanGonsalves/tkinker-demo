import tkinter as tk

window = tk.Tk()
window.title("Rock-Paper-Scissors")
window.geometry("400x300")
frame1= tk.Frame(window)
frame1.grid(column=0,row=0)
frame2 = tk.Frame(window)
frame2.grid(column=0,row=1)


window.mainloop()
