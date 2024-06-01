import tkinter as tk

window = tk.Tk()
window.title("My First Tkinker GUI")
label_name = tk.Label(text = "hello")
label_name.grid(column=0,row=0)

window.geometry('1000x600')
window.mainloop()
