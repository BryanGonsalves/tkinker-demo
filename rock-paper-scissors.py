import tkinter as tk

window = tk.Tk()
window.geometry("400x300")
window.title("Rock Paper Scissors Game")


USER_SCORE = 0
COMP_SCORE = 0
USER_CHOICE = ""
COMP_CHOICE = ""

def random_computer_choice():
    return random.choice(['rock','paper','scissors'])

def result(x,y):
    print("We will define it soon...")

def rock():
    global USER_CHOICE
    global COMP_CHOICE
    USER_CHOICE='rock'
    COMP_CHOICE=random_computer_choice()
    result(USER_CHOICE,COMP_CHOICE)
def paper():
    global USER_CHOICE
    global COMP_CHOICE
    USER_CHOICE='paper'
    COMP_CHOICE=random_computer_choice()
    result(USER_CHOICE,COMP_CHOICE)
def scissors():
    global USER_CHOICE
    global COMP_CHOICE
    USER_CHOICE='scissors'
    COMP_CHOICE=random_computer_choice()
    result(USER_CHOICE,COMP_CHOICE)


frame1 = tk.Frame(window, padx=5, pady=5)
frame1.grid(column=0,row=0)

frame2 = tk.Frame(window)
frame2.grid(column=1,row=0)

text_area = tk.Text(master=frame1,height=12,width=30,padx=10,pady=10,bg="#CAD5E2")
text_area.grid(column=0,row=0)
text_area.insert(tk.END,"\n\nYour Score : 0 \nComputer Score : 0 \n \nClick on any button to start.")

button1 = tk.Button(frame2,text="      Rock     ",background="#50DBB4",padx=20,pady=25)
button1.grid(column=0,row=0)
button2 = tk.Button(frame2,text="     Paper    ",background="#50DBB4",padx=20,pady=25)
button2.grid(column=0,row=1)
button3 = tk.Button(frame2,text="   Scissors  ",background="#50DBB4",padx=20,pady=25)
button3.grid(column=0,row=2)

window.mainloop()
