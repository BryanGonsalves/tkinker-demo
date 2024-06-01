import tkinter as tk

window = tk.Tk()
window.title("My First Tkinker GUI")
label_name = tk.Label(text = "Hello, this is my first Tkinter App!")
button_name = tk.Button(window,text="Click Me!")
label_name.grid(column=0,row=0)
button_name.grid(column=1,row=0)


window.geometry('1000x1000')
window.mainloop()
