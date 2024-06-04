import tkinter as tk

window = tk.Tk()
window.title("Registration Form")
window.geometry("600x400")

def printData():
    print(fNameEntry.get())
    print(lNameEntry.get())
    print(addressText.get("1.0","end"))
    print(nationVar.get())
    print(genderVar.get())
    print(termsVar.get())

button=tk.Button(window,text="Submit",command=printData)
button.grid(column=0,row=6)



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

nationLabel = tk.Label(text="Nationality: ")
nationLabel.grid(column=0,row=3)
nationVar = tk.StringVar(window)
nationVar.set("Select")
opMenu = tk.OptionMenu(window, nationVar, "US","UK", "India")
opMenu.grid(column=1,row=3)

genderLabel = tk.Label(text="Gender: ")
genderLabel.grid(column=0,row=4)
genderVar = tk.StringVar()
R1 = tk.Radiobutton(window,text="Male",variable=genderVar, value='Male')
R1.grid(column=1,row=4)
R2 = tk.Radiobutton(window, text="Female", variable=genderVar, value='Female')
R2.grid(column=2,row=4)
termsVar = tk.IntVar()
C1 = tk.Checkbutton(window, text = "I agree to T & C", variable = termsVar, \
                 onvalue = 1, offvalue = 0, height=2, \
                 width = 17)
C1.grid(column=1,row=5)

window.mainloop()