import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Style
import pyttsx3

r=0
def get_range():
    r=int(entry2.get())
    print(r)
    return r


voice=0
def show_selected():
    selected_option=var.get()
    print(selected_option)
    if selected_option == "Female":
        voice=1
    else:
        voice=0
    return voice
def get_text():
    text = entry.get(1.0,"end-1c")
    if text=="":
        messagebox.showerror("Error","Enter something in the text box to get the result")
    convert(text)

def convert(text):
    v=show_selected()

    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[v].id)
    engine.setProperty('rate', get_range())
    engine.say(text)
    engine.runAndWait()


win=Tk()
win.title("Text Talker")
win.geometry("700x350")
win.configure(bg='light blue')
style = Style()
style.configure('TRadiobutton', font=('Arial', 12))

# Set text and background colors for the radio buttons
style.configure('TRadiobutton', foreground='blue', background='lightgrey')




label = Label(win, text="Text Talker", font=('BOLD', 40),bg="white",fg="black")
label.place(x=650,y=10)

entry=Text(win,height=30,width=70,borderwidth=10,)
entry.place(x=100,y=100)



label2=Label(win,text="Choose a voice",font=('',20))
label2.place(x=800,y=300)

label3=Label(win,text="Number of words per minute",font=('',20),bg='lightblue')
label3.place(x=800,y=500)

entry2=Text(win,height=2,width=10,bg='lightblue',borderwidth=1)
entry2.place(x=1150,y=500)

options = [
    "Male \n\n",
    "Female\n\n"
]

# Determine the height for all radio buttons
button_height = 3
button_width = 20
var = StringVar()

# Create radio buttons for each option and set their height
for i, option in enumerate(options):
    radio_button = Radiobutton(win, text=option, variable=var, value=option.strip(), command=show_selected,width=button_width, height=button_height)
    radio_button.place(x=1000, y=300 + 60*i)

var.set(options[0])

b1 = Button(win, text="speak",bg="black",fg="white",width=25,height=3,command=get_text)
b1.place(x=300,y=650)


win.mainloop()