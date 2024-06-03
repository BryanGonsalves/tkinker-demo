import tkinter as tk

window=tk.Tk()
window.title(" My Window ")
window.geometry("600x400")

opLabel = tk.Label(text = "Select the Option: ")
opLabel.grid(column=0,row=0)

myVar  = tk.StringVar(window)
myVar.set("Select")
opMenu = tk.OptionMenu(window, myVar, "Option1","Option2", "Option3")
opMenu.grid(column=1,row=0)

def printOption():
    value = myVar.get()
    print(value)

button=tk.Button(window,text="Click Here",command=printOption)
button.grid(column=0,row=1)

window.mainloop()
