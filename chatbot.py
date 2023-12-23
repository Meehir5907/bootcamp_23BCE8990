from tkinter import *
from pydub import AudioSegment as Ads
from pydub.playback import play
from datetime import datetime

def chbt(event=None):
    D=t.get()
    user_input = t.get().strip()
    user_input = user_input.lower()
    
    if user_input in ["quit", "exit", "q"]:
        print("Terminating process\nBye!")
        r.destroy()
    else:
        add_message("You", D)
        process_input(user_input)
        t.delete(0, END)

def add_message(sender, message):
    current_time = datetime.now().strftime("%H:%M")
    conv.config(state=NORMAL)
    conv.insert(END, f"{sender} ({current_time}):\n", "time")
    conv.insert(END, f"{message}\n")
    conv.insert(END, '\n')
    conv.config(state=DISABLED)
    conv.see(END)

def process_input(user_input):
    if "hello" in user_input:
        s = Ads.from_mp3("r1.mp3")
        add_message("Mechbt", "Hello my friend")
        play(s)
    elif "how are you" in user_input:
        s = Ads.from_mp3("r2.mp3")
        add_message("Mechbt", "I am fine, how are you?")
        play(s)
    elif "i'm fine" in user_input or "i am fine" in user_input:
        s = Ads.from_mp3("r3.mp3")
        add_message("Mechbt","Its nice to hear that!")
        play(s)
    elif (("do" in user_input) and ("calculation" in user_input)) or ("calculate" in user_input):
        s = Ads.from_mp3("r4.mp3")
        add_message("Mechbt(calculator)", "Very well")
        add_message("Mechbt(calculator)", "Please enter the mathematical expression.")
        t.delete(0,END)
        t.bind("<Return>", lambda event: calc_expr())
        
def calc_expr():
    try:
        expression = t.get()
        add_message("You", expression)
        result = calculate(expression)
        add_message("Mechbt(calculator)", result)
        t.bind("<Return>",chbt)
    except Exception as e:
        add_message("Mechbt(calculator)", "Invalid expression. Please enter a valid mathematical expression.")
        t.bind("<Return>",chbt)
def calculate(expr):
    try:
        result = eval(expr)
        return f"The result is {result}"
    except Exception as e:
        raise e

r = Tk()
r.geometry("300x600")
r.title("Mechbt")
r.configure(bg="black")

frame = Frame(r)
frame.pack(fill=BOTH, expand=True)
frame.configure(bg="black")

conv = Text(frame, wrap=WORD)
conv.pack(fill=BOTH, expand=True, padx=10, pady=10)
conv.configure(bg="gray")
conv.tag_configure("time", foreground="white")

t = Entry(r, width=10)
t.pack(fill=X, padx=10, pady=5)
t.bind("<Return>", chbt)
t.configure(bg="grey",fg="white")

b = Button(r, text="Send", command=chbt)
b.pack(padx=10, pady=5)
b.configure(background="#EDB525")

r.mainloop()
