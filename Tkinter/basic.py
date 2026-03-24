from tkinter import *

win = Tk()
win.title("TKinter")
win.geometry('1000x1000+500+300')

# Label

L=Label(win,text="Hello World")
L.pack()

#Button

b=Button(win, text="Click me")
b.pack()

# Input Field

l=Label(win,text="Name")
l.pack()
e=Entry(win)
e.pack()

# Big Input Field

text=Text(win, width=30, height=10)
text.pack()

#Radio & Check button

c=Checkbutton(win, text='Yes')
c.pack()

c1=Radiobutton(win, text='Option1',variable='v1',value=1)
c1.pack()
c2=Radiobutton(win, text='Option1',variable='v1',value=2)
c2.pack()
c3=Radiobutton(win, text='Option3',variable='v1',value=3)
c3.pack()

# Option Menu 

v =StringVar()
o =OptionMenu(win, v, 'Python',*('Java','C++','Python','JavaScript'))
o.pack()

win.mainloop()