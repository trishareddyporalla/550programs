from tkinter import *
from tkinter import messagebox


def fact():
    n=int(numberEntry.get())
    factorial = 1
    for i in range(1,n+1):
        factorial*=i
    ans=str(factorial)
    answerlabel=Label(frame,text="factorial of given number is "+ans,height=10)
    answerlabel.grid(row=3,column=1)





window=Tk()
frame=Frame(window)
window.title("factorial")
frame.place(x=600,y=100)

label = Label(frame,text="Enter a number")
label.grid(row=1,column=1)
numberEntry = Entry(frame,width=20)
numberEntry.grid(row=1,column=2)

submitButton = Button(frame,text="submit",command=fact)
submitButton.grid(row=2,column=1)


window.mainloop()