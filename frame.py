import tkinter as tk

window=tk.Tk()
window.title("My Window")
window.geometry("300x300")

frame1 = tk.Frame(window)
frame1.grid(column=0,row=0,padx=20)

frame2 = tk.Frame(window)
frame2.grid(column=1,row=0)

myText = tk.Text(frame1,height=10,width=20)
myText.grid(column=0,row=0)

myLabel = tk.Label(frame2,text="Hello World")
myLabel.grid(column=0,row=0)

myButton = tk.Button(frame2, text ="Click Here")
myButton.grid(column=0,row=1)

window.mainloop()
