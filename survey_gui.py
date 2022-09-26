from multiprocessing import Event
from operator import concat
from sqlite3 import Row
from textwrap import fill
import tkinter as tk
from tkinter import ttk
from tkinter.tix import COLUMN
from tkinter.messagebox import showinfo
from tkinter import filedialog
#from typing import Literal, Text
root = tk.Tk()
root.title("survey")

entryNameValue = tk.StringVar()
current_value = tk.StringVar(value=0)
gender_var = tk.StringVar()
entryPlaceValue=tk.StringVar()
currentjob_var=tk.StringVar()
expJob= ('Data scientist', 'Developer', 'Machine Learning Engineer', 'Research Engineer', 'Python Developer',
        'Algorithm Developer')
expJob_var = tk.StringVar(value=expJob)
marriedValue = tk.StringVar() 

b=open("message.txt","r")
lines = b.readlines()
print(lines)
b.close()

name=lines[0]
name1=name.split(":")
print(name1)
name2=name1[1]
print(name2)
entryNameValue.set(name2)

age=lines[1]
print(age)
age1=age.split(":")
print(age1)
age2=age1[1]
print(age2)
current_value.set(age2)

gender=lines[2]
gender1=gender.split(":")
gender2=gender1[1]
print(gender2)
#if gender2 == 'gender2':
    #gender_var.select()
gender_var.set(gender2.strip())

place=lines[3]
place1=place.split(":")
place2=place1[1]
print(place2)
entryPlaceValue.set(place2)

curjob=lines[4]
curjob1=curjob.split(":")
curjob2=curjob1[1]
print(curjob2)
currentjob_var.set(curjob2)

expJob=lines[5]
expJob1=expJob.split(":")
expJob2=expJob1[1]
print(expJob2)
expJob_var.set(expJob2)

married=lines[6] 
married1=married.split(":") 
married2=married1[1] 
print(married)
if married2 == 'yes':
    marriedValue.select() 
#marriedValue.set(married)
'''
def split(name,age,gender,place,job,expejob,mar):
    for i in lines:
        c=lines.split(":")
        print(c)

print(str(split(entryNameValue,current_value,gender_var,entryPlaceValue,currentjob_var,expJob_var,marriedValue)))
'''        




labelHeading = tk.Label(root, text="JOB SURVEY FORM",font=("Times New Roman",20)).grid(column=2,row=1)
labelName = tk.Label(root, text="Name:",font=("Times New Roman", 15)).grid(column=1, row=2)
labelAge = tk.Label(root, text="Age:",font=("Times New Roman", 15)).grid(column=1, row=3)
labelGender = tk.Label(root, text="Gender:",font=("Times New Roman", 15)).grid(column=1, row=4)
labelPlace = tk.Label(root, text="Place:",font=("Times New Roman", 15)).grid(column=1, row=5)
labelCurrentJob = tk.Label(root, text="Current Job:",font=("Times New Roman", 15)).grid(column=1, row=6)
labelExpectedJob = tk.Label(root, text="Expected Job:",font=("Times New Roman", 15)).grid(column=1, row=7)
labelMarried = tk.Label(root, text="Married:",font=("Times New Roman", 15)).grid(column=1, row=8)



#entryNameValue = tk.StringVar()
entryTextName = ttk.Entry(root, textvariable=entryNameValue).grid(column=2, row=2,padx=10)

#current_value = tk.StringVar(value=0)
spinboxAge= tk.Spinbox(root,from_=0,to=60,textvariable=current_value,wrap=False).grid(column=2, row=3,padx=10)

#gender_var = tk.StringVar()
radioboxMale = tk.Radiobutton(root, text="Male", value="Male", variable=gender_var).grid(column=2, row=4, padx=10)
radioboxFemale = tk.Radiobutton(root, text="Female", value="Female", variable=gender_var).grid(column=3, row=4, padx=10)
radioboxOthers = tk.Radiobutton(root, text="others", value="Others", variable=gender_var).grid(column=4, row=4, padx=10)

#ntryPlaceValue=tk.stringvar()
entryTextPlace=ttk.Entry(root,textvariable=entryPlaceValue).grid(column=2, row=5,padx=10)
#textPlace= tk.Text(root, width=20, height=1).grid(column=2, row=5,padx=10)

#currentjob_var=tk.StringVar()
comboboxJobCurrentJob = ttk.Combobox(root, width = 27, textvariable =currentjob_var)
comboboxJobCurrentJob ['values'] = (' Doctor','Engineer',' Teacher',' Postman',' Clerk',' Accounter',' bank Manager',' Bussiness')
comboboxJobCurrentJob .grid(column = 2, row = 6)
comboboxJobCurrentJob .current()                         
                          

#expJob= ('Data scientist', 'Developer', 'Machine Learning Engineer', 'Research Engineer', 'Python Developer',
#        'Algorithm Developer')
#expJob_var = tk.StringVar(value=expJob)
listboxExpJob = tk.Listbox(root,listvariable=expJob_var,height=7,bg = "grey",fg="white",font=5,selectmode='extended')
listboxExpJob.grid(column=2,row=7)

#marriedValue = tk.StringVar()    
checkButtonMarried = tk.Checkbutton(root, text = "Yes", variable = marriedValue, onvalue = "Yes",offvalue = "No",height = 2,width = 10)
checkButtonMarried.grid(column=2,row=8)


iAgreeValue = tk.StringVar()    
checkButtonAgree = tk.Checkbutton(root, text = "I Agree", variable = iAgreeValue, onvalue = "agree",offvalue = "disagree",height = 2,width = 10)
checkButtonAgree.grid(column=1,row=9)


#####textpage=("Name: ",entryNameValue.get(),"Age: "gender_var.get(),"currentjob: "currentjob_var.get(),"expjob:"selected_langs,"married: "marriedValue.get())
######a=("Name: ",entryNameValue.get())

def click(event):
    print("Save")
    if iAgreeValue.get()=="agree":   
        selectedItem = listboxExpJob.curselection()
        selected_langs = ",".join([listboxExpJob.get(i) for i in selectedItem])
        #print(marriedValue.get())
        tk.messagebox.showinfo(title="result",message=(entryNameValue.get(),current_value.get(),gender_var.get(),entryPlaceValue.get(),currentjob_var.get(),selected_langs,marriedValue.get()))
        a="Name:"+entryNameValue.get()+"\n"+"Age:"+current_value.get()+"\n"+"Gender: "+gender_var.get()+"\n"+"Place: "+entryPlaceValue.get()+"\n"+"CurrentJob: "+currentjob_var.get()+"\n"+"Expectedjob: "+selected_langs+"\n"+"Married: "+marriedValue.get()+"\n"
        f=open("message.txt","w")
        f.write(a)
        f.close()   
    else:
        print("not")
    
    
btn = tk.Button(root, text='Save')
btn.grid(column=4,row=10)
btn.bind('<Button-1>',click)
btn.focus()
    
root.mainloop()


