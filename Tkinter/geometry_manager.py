from tkinter import *

win = Tk()
win.title("TKinter")
win.geometry('600x600')

b1=Button(win, text='button1', bg='lightblue', fg='blue')
b2=Button(win, text='button2', bg='lightblue', fg='blue')
b3=Button(win, text='button3', bg='lightblue', fg='blue')


b1.place(relx=0.5,rely=0.5, relwidth=0.20,relheight=0.1)
# b2.place(x=250,y=200, width=150,height=100)
# b3.place(x=400,y=300, width=150,height=100)








win.mainloop()
