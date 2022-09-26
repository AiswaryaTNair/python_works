
import tkinter as tk
from tkinter import ttk


def return_pressed(event):
    print('Return key pressed.')


def log(event):
    print(event)

def click(event):
    print("start quiz")

def clicked():
    print("start")



root = tk.Tk()

btn = ttk.Button(root, text='Save',command=clicked)
#btn.bind('<Return>', return_pressed)
#btn.bind('<Return>', log, add='+')
btn.bind('<Button-1>',click)


btn.focus()
btn.pack(expand=True)

root.mainloop()

#button creation
'''
def select(option):
    print(option)

ttk.Button(root, text='Rock', command=lambda: select('Rock')).pack()
ttk.Button(root, text='Paper',command=lambda: select('Paper')).pack()
ttk.Button(root, text='Scissors', command=lambda: select('Scissors')).pack()
...
