
from tkinter import *

win = Tk()
win.title("TKinter")
win.geometry('600x600')

b1 = Button(win, text='Button 1', highlightbackground='red', highlightthickness=3,highlightcolor='yellow')
b1.pack()

b2 =Button(win, text='Button 2')
b2.pack()



win.mainloop()