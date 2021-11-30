from pypresence import Presence
import pypresence
import tkinter
from tkinter import *
window = Tk()
window.title("RICH PRESENCE DISCORD")
window.geometry('210x200')
window.configure(background = "orange")
a = Label(window ,text = "State").grid(row = 0,column = 0)
b = Label(window ,text = "details").grid(row = 1,column = 0)
c = Label(window ,text = "button 1 name").grid(row = 2,column = 0)
d = Label(window ,text = "button 1 url").grid(row = 3,column = 0)
e = Label(window ,text = "button 2 name").grid(row = 4,column = 0)
f = Label(window ,text = "button 2 url").grid(row = 5,column = 0)
g = Label(window ,text = "Client_id").grid(row = 6,column = 0)
a1 = Entry(window)
a1.grid(row = 0,column = 1)
b1 = Entry(window)
b1.grid(row = 1,column = 1)
c1 = Entry(window)
c1.grid(row = 2,column = 1)
d1 = Entry(window)
d1.grid(row = 3,column = 1)
e1 = Entry(window)
e1.grid(row = 4,column = 1)
f1 = Entry(window)
f1.grid(row = 5,column = 1)
g1 = Entry(window)
g1.grid(row = 6,column = 1)


def callbackwithapropername():
    RPC = Presence(int(g1.get()))
    RPC.connect()
    print(RPC.update(state=a1.get(), details=b1.get(), buttons=[{"label": c1.get(), "url": d1.get()},{"label":e1.get(),"url":f1.get()}]))

submit = tkinter.Button(window, text="Confirm", command=callbackwithapropername)
submit.grid(row=8,column=0)





window.mainloop()