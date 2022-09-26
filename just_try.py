from sqlite3 import Row
from textwrap import fill
import tkinter as tk
from tkinter import ttk
from tkinter.tix import COLUMN
#from typing import Literal, Text
root = tk.Tk()
root.title("survey")
labelHeading = ttk.Label(root, text="JOB SURVEY FORM",font=("Times New Roman",20)).grid(column=2,row=1)

labelName = ttk.Label(root, text="Name:",font=("Times New Roman", 15)).grid(column=1, row=2)
labelAge = ttk.Label(root, text="Age:",font=("Times New Roman", 15)).grid(column=1, row=3)
labelGender = ttk.Label(root, text="Gender:",font=("Times New Roman", 15)).grid(column=1, row=4)

labelPlace = ttk.Label(root, text="Place:",font=("Times New Roman", 15)).grid(column=1, row=5)
labelCurrentJob = ttk.Label(root, text="Current Job:",font=("Times New Roman", 15)).grid(column=1, row=6)
labelExpectedJob = ttk.Label(root, text="Expected Job:",font=("Times New Roman", 15)).grid(column=1, row=7)


textName= ttk.Text(root, width=20, height=1).grid(column=2, row=2,padx=10)
current_value = ttk.StringVar(value=0)
spinboxAge= ttk.Spinbox(root,from_=0,to=60,textvariable=current_value,wrap=False).grid(column=2, row=3,padx=10)
'''
selected = tk.StringVar()
radioboxMale = tk.Radiobutton(root, text='Male', value='Male', variable=selected).grid(column=2, row=4,padx=10,sticky="W")
radioboxFemale= tk.Radiobutton(root, text='Female', value='Female', variable=selected).grid(column=2, row=4,padx=10,sticky="W")
radioboxOthers= tk.Radiobutton(root, text='Others', value='Others', variable=selected).grid(column=2, row=4,padx=10,sticky="W")
'''
##LabelFrameGender=tk.LabelFrame(root, text='Gender').grid(column=2, row=4, padx=10)
Gender_var = ttk.StringVar()
##Gender = ('Left', 'Center', 'Right')

radioboxMale = ttk.Radiobutton(root, text="Male", value="Male", variable=Gender_var).grid(column=2, row=4, padx=10)
radioboxFemale = ttk.Radiobutton(root, text="Female", value="Female", variable=Gender_var).grid(column=3, row=4, padx=10)
radioboxOthers = ttk.Radiobutton(root, text="others", value="Others", variable=Gender_var).grid(column=4, row=4, padx=10)

textPlace= ttk.Text(root, width=20, height=1).grid(column=2, row=5,padx=10)
#textCurrentJob= tk.Text(root, width=20, height=1).grid(column=2, row=6,padx=10)
currentjob_var=ttk.StringVar()
Jobchoosen = ttk.Combobox(root, width = 27, textvariable =currentjob_var)
Jobchoosen['values'] = (' Doctor','Engineer',' Teacher',' Postman',' Clerk',' Accounter',' bank Manager',' Bussiness').grid(column = 2, row = 6)
Jobchoosen.current()                         
                          
                          
                          
                          
                          
                          


textExpectedJob= ttk.Text(root, width=20, height=1).grid(column=2, row=7,padx=10)
root.mainloop()
