from tkinter import *
from tkinter import messagebox

def GreatestOfTwo():
    n = int(num1Entry.get())
    m = int(num2Entry.get())
    o = int(num3Entry.get())
    if n >= m and n >= m:
        messagebox.showinfo("MAX OF THREE NUMBERS", f"NUM-1 ({n}) IS GREATER")
    elif m >= n and m >= o:
        messagebox.showinfo("MAX OF THREE NUMBERS", f"NUM-2 ({m}) IS GREATER")
    else:
        messagebox.showinfo("MAX OF THREE NUMBERS", f"NUM-3 ({o}) IS GREATER")

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

label2 = Label(frame,text="Enter a number")
label2.grid(row=3,column=1)
num3Entry = Entry(frame,width=20)
num3Entry.grid(row=3,column=2)


submitButton = Button(frame,text="submit",command=GreatestOfTwo)
submitButton.grid(row=4,column=1)


window.mainloop()