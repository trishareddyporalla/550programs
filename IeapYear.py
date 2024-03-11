from tkinter import *

def isit():
    n=int(yearEntry.get())
    if n%400 ==0 :
        ansLabel = Label(frame,text="Given year is a leap year")
        ansLabel.grid(row=3,column=1)
    elif n%100 ==0:
        ansLabel = Label(frame, text="Given year is not a leap year")
        ansLabel.grid(row=3, column=1)
    elif n%4==0 :
        ansLabel = Label(frame, text="Given year is a leap year")
        ansLabel.grid(row=3, column=1)
    else:
        ansLabel = Label(frame, text="Given year is not a leap year")
        ansLabel.grid(row=3, column=1)


window=Tk()
frame=Frame(window)
frame.place(x=100,y=100)
window.title("leap year or not")

label1 =Label(frame,text="enter an year")
label1.grid(row=1,column=1)

yearEntry =Entry(frame,width=10)
yearEntry.grid(row=1,column=2)

submit=Button(frame,text="submit",command=isit)
submit.grid(row=2,column=2)

window.mainloop()