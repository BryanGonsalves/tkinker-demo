import tkinter as tk

window = tk.Tk()
window.title("Rock-Paper-Scissors")
window.geometry("400x300")
frame1= tk.Frame(window)
frame1.grid(column=0,row=0)
frame2 = tk.Frame(window)
frame2.grid(column=0,row=1)

text_area = tk.Text(master=frame1,height=12,width=30,padx=10,pady=10,bg="#CAD5E2")
text_area.grid(column=0,row=0)
text_area.insert(tk.END,"\n\nYour Score: 0 \n\nComputer Score: 0\n\nClick on Any Button to Start.")


window.mainloop()
