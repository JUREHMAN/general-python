'''
This is a simple python program to create a GUI interface for a school fee submission system.
It has four buttons
Submit button submits the data entered  by the user
Clear button clear all the entries previously filled
Record button shows the record of previous submiited fee
Close button closed this application 
'''

from tkinter import *
import tkinter as tk
from tkinter import ttk

root = Tk()
root.title("School Fee System")
root.geometry("500x400")

#Creating a text file for storing the record
file1 = open("fee.txt",'a')

#Data for submission
#Name
name_label = ttk.Label(root, text="Name")
name_label.grid(column=8, row=2, sticky=tk.W, padx=5, pady=5)

name_entry = ttk.Entry(root)
name_entry.grid(column=9, row=2, sticky=tk.E, padx=5, pady=5)

#Father name
fname_label = ttk.Label(root, text="Father Name")
fname_label.grid(column=8, row=3, sticky=tk.W, padx=5, pady=5)

fname_entry = ttk.Entry(root)
fname_entry.grid(column=9, row=3, sticky=tk.E, padx=5, pady=5)

#Class
class_label = ttk.Label(root, text="Class")
class_label.grid(column=8, row=4, sticky=tk.W, padx=5, pady=5)

class_entry = ttk.Entry(root)
class_entry.grid(column=9, row=4, sticky=tk.E, padx=5, pady=5)

#Roll Number

roll_number_label = ttk.Label(root, text="Roll Number")
roll_number_label.grid(column=8, row=5, sticky=tk.W, padx=5, pady=5)

roll_number_entry = ttk.Entry(root)
roll_number_entry.grid(column=9, row=5, sticky=tk.E, padx=5, pady=5)

#Month

month_label = ttk.Label(root, text="Month")
month_label.grid(column=8, row=6, sticky=tk.W, padx=5, pady=5)

month_entry = ttk.Entry(root)
month_entry.grid(column=9, row=6, sticky=tk.E, padx=5, pady=5)

#Total Fee

total_fee_label = ttk.Label(root, text="Total Fee")
total_fee_label.grid(column=8, row=7, sticky=tk.W, padx=5, pady=5)

total_fee_entry = ttk.Entry(root)
total_fee_entry.grid(column=9, row=7, sticky=tk.E, padx=5, pady=5)

#Fee PAID
paid_fee_label = ttk.Label(root, text="Paid Fee")
paid_fee_label.grid(column=8, row=8, sticky=tk.W, padx=5, pady=5)

paid_fee_entry = ttk.Entry(root)
paid_fee_entry.grid(column=9, row=8, sticky=tk.E, padx=5, pady=5)

#Remaining Fee

remaining_fee_label = ttk.Label(root, text="Remainig Fee")
remaining_fee_label.grid(column=8, row=9, sticky=tk.W, padx=5, pady=5)

remaining_fee_entry = ttk.Entry(root)
remaining_fee_entry.grid(column=9, row=9, sticky=tk.E, padx=5, pady=5)

#comments

comments_label = ttk.Label(root, text="Comments")
comments_label.grid(column=8, row=10, sticky=tk.W, padx=5, pady=5)

comments_entry = ttk.Entry(root)
comments_entry.grid(column=9, row=10, sticky=tk.E, padx=5, pady=5)

#Function for submitting the fee
def func1a():
    #Input from the user
    name = name_entry.get()
    fname = fname_entry.get()
    rolnumber = roll_number_entry.get()
    clas = class_entry.get()
    month = month_entry.get()
    tf = total_fee_entry.get()
    pf = paid_fee_entry.get()
    rf = remaining_fee_entry.get()
    com = comments_entry.get()

    if len(name) >= 3 and len(fname) >= 3 and len(rolnumber) >= 1 and len(clas) >= 1 and len(month) >= 1 and len(tf) >= 2 and len(pf) >= 1 and len(rf) >= 1 and len(com) >= 1:
        with open('fee.txt','a') as f:
            f.write(name)
            f.write(',')
            f.write(fname)
            f.write(',')
            f.write(rolnumber)
            f.write(',')
            f.write(clas)
            f.write(',')
            f.write(month)
            f.write(',')
            f.write(tf)
            f.write(',')
            f.write(pf)
            f.write(',')
            f.write(rf)
            f.write(',')
            f.write(com)
            f.write('\n')
            label = Label(root, text= f"You submitted the fee of student {name} successfully")
            label.grid(columnspan=10, row=14, sticky=tk.W, padx=5, pady=5)
    else:
            label = Label(root, text= f"Please Fill all the required entries and then Submit to the record")
            label.grid(columnspan=10, row=14, sticky=tk.W, padx=5, pady=5)

#Function for showing the Record of the previous submissions
def func2():
    with open('fee.txt','r') as f1:
        label1 = Label(root, text=f1.readlines())
        label1.grid(columnspan=10, row=11, sticky=tk.W, padx=5, pady=5)


#Function for clearing the previosuly filled entries
def func3():
    name_entry.delete(0,END)
    fname_entry.delete(0,END)
    roll_number_entry.delete(0,END) 
    class_entry.delete(0,END)
    month_entry.delete(0,END)
    total_fee_entry.delete(0,END)
    paid_fee_entry.delete(0,END)
    remaining_fee_entry.delete(0,END) 
    comments_entry.delete(0,END)

#Submit Button
submit_data = ttk.Button(root,text="Submit",command=func1a)
submit_data.grid(column = 4,row = 2,sticky = tk.N,padx=5,pady=5)

#Record of Submission
record_data = ttk.Button(root,text="Record",command=func2)
record_data.grid(column = 4,row = 3,sticky = tk.N,padx=5,pady=5)

#Clear Screen
clear_data = ttk.Button(root,text="Clear Data",command=func3)
clear_data.grid(column = 4,row = 4,sticky = tk.N,padx=5,pady=5)

#Close App
submit_data = ttk.Button(root,text="Close",command=root.destroy)
submit_data.grid(column = 4,row = 5,sticky = tk.N,padx=5,pady=5)

#For execution of whole program
root.mainloop()