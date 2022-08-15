'''
This will be a simple contact book which will have initially 
three functions
displaying the list
saving the contact
closing the book
'''

from tkinter import *
from tkinter import ttk
import tkinter as tk

root = Tk()
root.title("Contact Book")
root.geometry("500x600")

#Creating a text file for keeping the record of contacts
file1 = open("contacts.txt","a")

#List function
def func1():
    #scroll bar setting
    win = Tk()
    win.geometry("290x600")
    win.resizable(0,0)
    win.title("Contact List")
    s = Scrollbar(win)
    scrollbar = ttk.Scrollbar(win, orient= 'vertical')
    scrollbar.pack(side= RIGHT, fill= BOTH)

    #Add a Listbox Widget
    listbox = Listbox(win, width= 350, font= ('Helvetica 12'))
    listbox.pack(side= LEFT, fill= BOTH)
    with open('contacts.txt','r') as f2:
        for line in f2:
            listbox.insert(END, f2.readline())
            listbox.config(yscrollcommand= scrollbar.set)

    scrollbar.config(command= listbox.yview)

#New Contact function
def func2():
    #Data of contact
    #Name
    name_label = ttk.Label(root, text="Name")
    name_label.grid(column=8, row=3, sticky=tk.W, padx=5, pady=5)

    name_entry = ttk.Entry(root)
    name_entry.grid(column=9, row=3, sticky=tk.E, padx=5, pady=5)

    #Phone Number
    phone_number_label = ttk.Label(root, text="Mobile Number")
    phone_number_label.grid(column=8, row=4, sticky=tk.W, padx=5, pady=5)

    phone_number_entry = ttk.Entry(root)
    phone_number_entry.grid(column=9, row=4, sticky=tk.E, padx=5, pady=5)

    #Office Number
    office_number_label = ttk.Label(root, text="Office Number")
    office_number_label.grid(column=8, row=5, sticky=tk.W, padx=5, pady=5)

    office_number_entry = ttk.Entry(root)
    office_number_entry.grid(column=9, row=5, sticky=tk.E, padx=5, pady=5)
    
    #Save function
    def func1a():
        name = name_entry.get()
        number1 = phone_number_entry.get()
        number2 = office_number_entry.get()

        if len(name) >= 1 and len(number1) >= 9 and len(number2)>=0:
            with open('contacts.txt','a') as f:
                f.write(name)
                f.write(',')
                f.write(number1)
                f.write(',')
                f.write(number2)
                f.write('\n')
                label = Label(root, text= f"You have entered the contact of {name} successfully")
                label.grid(columnspan=10, row=10, sticky=tk.W, padx=5, pady=5)
        else:
            label = Label(root, text= f"Please Fill all the required entries and then Submit to the record")
            label.grid(columnspan=10, row=10, sticky=tk.W, padx=5, pady=5)

#Save button
    save = ttk.Button(root,text="Save",command=func1a)
    save.grid(column = 8,row = 7,sticky = tk.N,padx=5,pady=5)


#Creating Buttons
#List
contact_list = ttk.Button(root,text="List",command=func1)
contact_list.grid(column = 1,row = 1,sticky = tk.N,padx=5,pady=5)


#New contact
new_contact = ttk.Button(root,text="New Contact",command=func2)
new_contact.grid(column = 3,row = 1,sticky = tk.N,padx=5,pady=5)


#Closing the app
close_book = ttk.Button(root,text="CLose",command=root.destroy)
close_book.grid(column = 1,row = 8,sticky = tk.E,padx=5,pady=5)
root.mainloop()