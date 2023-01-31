from tkinter import *
gui=Tk(className="spam notification")
gui.geometry('500x300')
Label(text='Spam') .pack()
mainloop()

from tkinter import *
from tkinter.messagebox import showinfo

def reply():
    showinfo(title='popup', message='Button pressed!')
    
window = Tk(className="confirmtion")
window.geometry('500x300')
button = Button(window, text='press', command=reply)
button.pack()
window.mainloop()