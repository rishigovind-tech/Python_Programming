from tkinter import *

win = Tk()
win.title("TKinter")
win.geometry('600x400+500+300')

l =Button(win)
l['text']='Hello World'
l['bg']='red'
l['fg']='yellow'
l.config(font='Ariel, 20')

l.pack(pady=100)


win.mainloop()