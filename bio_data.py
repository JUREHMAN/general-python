'''
This is a simple bio data form which have two main(Enter Data and Clear) functions 
and a close function.
The program take the input from the user in GUI and store it in a text file.
'''

from tkinter import *
from tkinter import ttk
import tkinter as tk
root = Tk()
root.geometry('400x400')
root.title('SAMPLE BIO DATA FORM')

#File for storing the entered Data

file1 =open("biodata.txt",'a')

#defining functions

#Function to enter the values
def func1():
    name          = name_entry.get()
    father_name   = fname_entry.get()
    cnic          = cnic_entry.get()
    date_of_birth = dob_entry.get()
    gender        = gender_entry.get()
    profession    = profession_entry.get()
    
    with open('biodata.txt','a') as f:

        #checking whether all entries are filled or not
        if len(name) >= 3 and len(father_name) >= 3 and len(cnic) == 13 and len(date_of_birth) == 10 and len(gender) >= 4 and len(profession)>=3:
            f.write(name)
            f.write(',')
            f.write(father_name)
            f.write(',')
            f.write(cnic)
            f.write(',')
            f.write(date_of_birth)
            f.write(',')
            f.write(gender)
            f.write(',')
            f.write(profession)
            f.write('\n')
            label = Label(root, text= f"Your data Entered successfully")
            label.grid(columnspan=10, row=12, sticky=tk.W, padx=5, pady=5)
        else:
            label = Label(root, text= f"Some Entry is empty or not filled in the require format\nKindly try again")
            label.grid(columnspan=10, row=12, sticky=tk.W, padx=5, pady=5)

#Function to Clear the form
def func2():
    name_entry.delete(0,END)
    fname_entry.delete(0,END)
    cnic_entry.delete(0,END)
    dob_entry.delete(0,END)
    gender_entry.delete(0,END)
    profession_entry.delete(0,END)

'''
Buttons and Entries

'''
#Name
name_label = ttk.Label(root, text="Name")
name_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)

name_entry = ttk.Entry(root)
name_entry.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)

#Father Name

fname_label = ttk.Label(root,text='Father Name')
fname_label.grid(column=0,row=2,sticky=tk.W,padx=5,pady=5)

fname_entry = ttk.Entry(root)
fname_entry.grid(column=1,row=2,sticky=tk.E,padx=5,pady=5)

#C.N.I.C

cnic_label = ttk.Label(root,text='C.N.I.C Number (without -)')
cnic_label.grid(column=0,row=3,sticky=tk.W,padx=5,pady=5)

cnic_entry = ttk.Entry(root)
cnic_entry.grid(column=1,row=3,sticky=tk.E,padx=5,pady=5)

#D.O.B

dob_label = ttk.Label(root,text='D.O.B (dd/mm/yy)')
dob_label.grid(column=0,row=4,sticky=tk.W,padx=5,pady=5)

dob_entry = ttk.Entry(root)
dob_entry.grid(column=1,row=4,sticky=tk.E,padx=5,pady=5)

#Gender

gender_label = ttk.Label(root,text='Gender')
gender_label.grid(column=0,row=5,sticky=tk.W,padx=5,pady=5)

gender_entry = ttk.Entry(root)
gender_entry.grid(column=1,row=5,sticky=tk.E,padx=5,pady=5)

#Profession

profession_label = ttk.Label(root,text='Profession')
profession_label.grid(column=0,row=6,sticky=tk.W,padx=5,pady=5)

profession_entry = ttk.Entry(root)
profession_entry.grid(column=1,row=6,sticky=tk.E,padx=5,pady=5)


#Enter data button
enter_data = ttk.Button(root,text="Enter Data",command=func1)
enter_data.grid(column = 1,row = 8,sticky = tk.N,padx=5,pady=5)

#Clear Form button

clear_button = ttk.Button(root,text="Clear ",command=func2)
clear_button.grid(column = 1, row = 9,sticky = tk.N,padx=5,pady=5)

#Close Application button

close_button = ttk.Button(root,text="Close This App ",command=root.destroy)
close_button.grid(column = 1, row = 10,sticky = tk.N,padx=5,pady=5)

root.mainloop()