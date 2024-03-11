from tkinter import *
from tkinter import messagebox


def is_perfect_number():
    number=int(numberEntry.get())
    if number <= 0:
        return False

    sum_of_divisors = 0
    for i in range(1, number):
        if number % i == 0:
            sum_of_divisors += i

    if sum_of_divisors == number :
        label = Label(frame, text="given number is a perfect number")
        label.grid(row=3, column=1)
    else :
        label = Label(frame, text="given number is not a perfect number")
        label.grid(row=3, column=1)





window=Tk()
frame=Frame(window)
window.title("factorial")
frame.place(x=600,y=100)

label = Label(frame,text="Enter a number")
label.grid(row=1,column=1)
numberEntry = Entry(frame,width=20)
numberEntry.grid(row=1,column=2)

submitButton = Button(frame,text="submit",command=is_perfect_number)
submitButton.grid(row=2,column=1)


window.mainloop()