import tkinter as tk
from tkinter import *
mainwindow=tk.Tk()
mainwindow.title("calculator")
heading=tk.Label(mainwindow,text="calculation:")
heading.pack()

val1=tk.Entry(mainwindow)
val2=tk.Entry(mainwindow)
val1.pack()
val2.pack()

a=0
b=0

def takeinput():
    global a,b
    a = int(val1.get())
    b = int(val2.get())
    print(a)
    print(b)

def add():
    global a, b
    takeinput()
    c=a + b
    print(c)

def sub():
    global a, b
    takeinput()
    d = a - b
    print(d)

def mult():
    takeinput()
    e = a * b
    print(e)

def div():
    global a, b
    takeinput()
    f = a/b
    print(f)

buttond=tk.Button(mainwindow, text="+", command= lambda: add())
buttona=tk.Button(mainwindow, text= "-", command= lambda : sub())
buttonb=tk.Button(mainwindow, text= "/", command = lambda : div())
buttonc=tk.Button(mainwindow, text= "X", command = lambda: mult())

buttona.pack()
buttonb.pack()
buttonc.pack()
buttond.pack()


mainwindow.mainloop()
