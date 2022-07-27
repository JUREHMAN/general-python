from tkinter import *
import tkinter as tk
from tkinter import ttk
root = tk.Tk()
root.geometry("600x500")
root.title('AGE CALCULATOR')
#root.resizable(0, 0)

age=''
y=''
m=''
d=''
def calc():
    y2 = password_entry.get()
    y1 = username_entry.get()
    m1 = username_entry1.get()
    m2 = password_entry1.get()
    d1 = username_entry2.get()
    d2 = password_entry2.get()
    y = abs(int(y2) - int(y1))
    m = abs(int(m1) - int(m2))
    d = abs(int(d1) - int(d2))
    print("Your age is ",y," years and ",m," months ",d," days.")

# configure the grid
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=3)

# Birth Year
username_label = ttk.Label(root, text="Birth Year:")
username_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)

username_entry = ttk.Entry(root)
username_entry.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)

# Birth Month
username_label1 = ttk.Label(root, text="Birth Month:")
username_label1.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)

username_entry1 = ttk.Entry(root)
username_entry1.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)

# Birth Day
username_label2 = ttk.Label(root, text="Birth Day:")
username_label2.grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)

username_entry2 = ttk.Entry(root)
username_entry2.grid(column=1, row=2, sticky=tk.E, padx=5, pady=5)



# Current Year
password_label = ttk.Label(root, text="Currrent Year:")
password_label.grid(column=0, row=3, sticky=tk.W, padx=5, pady=5)

password_entry = ttk.Entry(root)
password_entry.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)

#Current MOnth
password_label1 = ttk.Label(root, text="Currrent Month:")
password_label1.grid(column=0, row=4, sticky=tk.W, padx=5, pady=5)

password_entry1 = ttk.Entry(root)
password_entry1.grid(column=1, row=4, sticky=tk.E, padx=5, pady=5)

#Current Day
password_label2 = ttk.Label(root, text="Currrent Day:")
password_label2.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)

password_entry2 = ttk.Entry(root)
password_entry2.grid(column=1, row=5, sticky=tk.E, padx=5, pady=5)

# login button
Calculate_your_age = ttk.Button(root, text="Calculate Your Age",command=calc)
Calculate_your_age.grid(column=1, row=6, sticky=tk.W, padx=5, pady=5)

root.mainloop()