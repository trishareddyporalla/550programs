from tkinter import *
from tkinter import messagebox

def GreatestOfTwo():
    n = int(num1Entry.get())
    m = int(num2Entry.get())
    if n>m :
        messagebox.showinfo(title="Greatest of two numbers is ",message=n)
    else:
        messagebox.showinfo(title="Greatest of two numbers is ",message=m)


window=Tk()
frame=Frame(window)
frame.place(x=600,y=100)

label = Label(frame,text="Enter a number")
label.grid(row=1,column=1)
num1Entry = Entry(frame,width=20)
num1Entry.grid(row=1,column=2)

label1 = Label(frame,text="Enter a number")
label1.grid(row=2,column=1)
num2Entry = Entry(frame,width=20)
num2Entry.grid(row=2,column=2)


submitButton = Button(frame,text="submit",command=GreatestOfTwo)
submitButton.grid(row=3,column=1)


window.mainloop()