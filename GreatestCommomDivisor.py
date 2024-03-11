from tkinter import *
from tkinter import messagebox
import math

def Gcdoftwo():
    a=int(num1Entry.get())
    b=int(num2Entry.get())
    c=math.gcd(a,b)
    ans=str(c)
    label = Label(frame, text="GCD of given two numbers is "+ans)
    label.grid(row=4, column=1)




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


submitButton = Button(frame,text="submit",command=Gcdoftwo)
submitButton.grid(row=3,column=1)


window.mainloop()