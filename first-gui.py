import tkinter as tk


def hello(event):
    display = tk.Label(text ="Hello User!")
    display.grid(column=0,row=2)
def bye(event):
    display2 = tk.Label(text="Bye User!")
    display2.grid(column=0,row=2)
    

window = tk.Tk()
window.title("My First Tkinker GUI")
label_name = tk.Label(text = "Hello, this is my first Tkinter App!")
button_name = tk.Button(window,text="Click Me!")
label_name.grid(column=0,row=0)
button_name.grid(column=1,row=0)
button_name.bind("<Button-1>",hello)
button_name.bind("<Button-2>",bye)


window.geometry('1000x600')
window.mainloop()
