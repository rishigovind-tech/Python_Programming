from tkinter import *
from tkinter.messagebox import *

def fun(e):
    print("Event is Generated")
    showinfo('My Box', 'Event is Generated')
    

win = Tk()
win.title("TKinter")
win.geometry('600x400')


e=Entry(win,bg='red',fg='yellow')
e.place(x=100,y=100,width=300,height=50)

e1=Entry(win,bg='red',fg='yellow')
e1.place(x=100,y=160,width=300,height=50)

e2=Entry(win,bg='red',fg='yellow')
e2.place(x=100,y=220,width=300,height=50)

win.bind_class('Entry','<Button-1>',fun)




win.mainloop()
