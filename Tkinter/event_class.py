from tkinter import *

def my_handler(e):
    print(e)
    print(e.state)
    print(e.x_root,e.y_root)



win = Tk()
win.title("TKinter")
win.geometry('600x600')

ent= Entry(win)
ent.pack()
ent.bind('<Button-1>',my_handler)



win.mainloop()





# from tkinter import *

# win = Tk()
# win.title("TKinter")
# win.geometry('600x600')


# win.mainloop()