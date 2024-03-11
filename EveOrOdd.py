from tkinter import *
from tkinter import messagebox

def number():
    n=int(numEntry.get())
    if n%2 == 0:
        messagebox.showinfo("given number is ","even        ")
    else:
        messagebox.showinfo("given number is ","odd          ")



window = Tk()
frame =Frame(window)
window.title("Even or odd")
frame.place(x=600,y=100)

numlabel = Label(frame,text="enter a number")
numlabel.grid(row=1,column=1)

numEntry = Entry(frame,width=30)
numEntry.grid(row=1,column=2)

Submit = Button(frame,text="submit",command=number,width=5)
Submit.grid(row=2,column=2)

window.mainloop()