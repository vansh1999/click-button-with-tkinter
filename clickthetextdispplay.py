from tkinter import *
window = Tk()
def printsearch():
    mtext= ment.get()
    mlabel= Label(window,text= mtext).pack()
    return
    

ment= StringVar() # string variable storage

window.geometry('500x200+200+200')
window.title('get what you write')
label = Label(text='welcome to our search engine',fg = 'orange',bg = 'white')
label.pack()

entry = Entry(window, text = ment).pack()

button = Button(window,text='search',command = printsearch , fg='white',bg='blue').pack()

window.mainloop()
