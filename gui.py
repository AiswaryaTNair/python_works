from doctest import master
from re import X
import tkinter as tk
from turtle import width
top = tk.Tk()

top.geometry("200x200+200+200")
message = tk.Label(top, text="Hello, World!",bg="blue")
message2=tk.Label(top,text="start quiz",bg="red")
message.pack(expand=1,fill=tk.BOTH)
message2.pack(expand=1,fill=tk.BOTH)
#message2=tk.Label(top,text="start quiz",bg="red").pack()    #or line 10
top.title("quiz master")
top.mainloop()
#top.resizable(False,False)


#### single button creation
#def button_clicked():
    #print('Button clicked')
#tk.Button(top, text='Click Me',command=button_clicked).pack()
#top.mainloop

####more than one button creation
#def select(option):
    #print(option)


#tk.Button(top, text='Rock', command=lambda: select('Rock')).pack()
#tk.Button(top, text='Paper',command=lambda: select('Paper')).pack()
#tk.Button(top, text='Scissors', command=lambda: select('Scissors')).pack()

#top.mainloop()



print('aaa')
'''
window_width = 300
window_height = 200

# get the screen dimension
screen_width = top.winfo_screenwidth()
screen_height = top.winfo_screenheight()

# find the center point
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

# set the position of the window to the center of the screen
top.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
top.mainloop()
'''

