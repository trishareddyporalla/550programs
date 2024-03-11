from tkinter import *
from tkinter import messagebox

def check():
    n=int(numEntry.get())
    if n>=18:
        messagebox.showinfo(title="eligibility",message="you are eligible to vote")
    else:
        messagebox.showerror(title="Eligibility check error",message="you are not eligible to vote as you're age is less than 18")


window=Tk()
frame=Frame(window)
frame.place(x=600,y=100)

label = Label(frame,text="Enter a number")
label.grid(row=1,column=1)
numEntry = Entry(frame,width=20)
numEntry.grid(row=1,column=2)

submitButton = Button(frame,text="submit",command=check)
submitButton.grid(row=2,column=1)


window.mainloop()