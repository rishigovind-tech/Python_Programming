from tkinter import *

win = Tk()
win.title("TKinter")
# win.geometry('600x400+500+300')

# l1 = Label(win, text='Label 1', bg='red',fg='black')
# l1.pack(side=LEFT)

# l2 = Label(win, text='Label 2', bg='red',fg='black')
# l2.pack(side=TOP)

# l3= Label(win, text='Label 3', bg='red',fg='black')
# l3.pack(side=RIGHT)




# l1 = Label(win, text='Label 1', bg='red',fg='black')
# l1.pack(anchor=NW)

# l2 = Label(win, text='Label 2', bg='red',fg='black')
# l2.pack(anchor=SE)

# l3= Label(win, text='Label 3', bg='red',fg='black')
# l3.pack(anchor=S)





# l1 = Label(win, text='Label 1', bg='red',fg='black')
# l1.pack(padx=2,pady=2,ipadx=5,ipady=5)

# l2 = Label(win, text='Label 2', bg='red',fg='black')
# l2.pack(padx=2,pady=2,ipadx=5,ipady=5)

# l3= Label(win, text='Label 3', bg='red',fg='black')
# l3.pack(padx=2,pady=2,ipadx=5,ipady=5)


l1 = Label(win, text='Label 1', bg='red',fg='black')
l1.pack(side=LEFT,fill=Y,padx=2,pady=2,ipadx=5,ipady=5)

l2 = Label(win,text='Label 2', bg='red',fg='black')
l2.pack(side=TOP,fill=X,padx=2,pady=2,ipadx=5,ipady=5)


l3= Label(win, text='Label 3', bg='red',fg='black')
l3.pack(side=LEFT,padx=2,pady=2,ipadx=5,ipady=5)

l4= Label(win, text='Label 4', bg='red',fg='black')
l4.pack(side=LEFT,padx=2,pady=2,ipadx=5,ipady=5)

win.mainloop()