import tkinter as tk

window = tk.Tk()
window.title("Registration Form")
window.geometry("600x400")

fNameLabel = tk.Label(text="First Name: ")
fNameLabel.grid(column=0,row=0)
fNameEntry = tk.Entry(window)
fNameEntry.grid(column=1,row=0)
lNameLabel = tk.Label(text="Last Name: ")
lNameLabel.grid(column=0,row=1)
lNameEntry = tk.Entry(window)
lNameEntry.grid(column=1,row=1)

addressLabel = tk.Label(text="Address: ")
addressLabel.grid(column=0,row=2)
addressText = tk.Text(window,height=4,width=15)
addressText.grid(column=1,row=2)



window.mainloop()