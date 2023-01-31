from tkinter import *
from oop_wiget import MyGui
# main app window
mainwin = Tk()
Label(mainwin, text= __name__ ).pack()
# popup window
popup = Toplevel()
Label(popup,text='Attach').pack(side=LEFT)
MyGui(popup).pack(side=RIGHT)
mainwin.mainloop()