from tkinter import *

def fun():
    print("Button is Clicked")

win = Tk()
win.title("TKinter")
win.geometry('600x400')


b1=Button(win, text='My Button', command=fun)
b1.pack()

win.mainloop()
