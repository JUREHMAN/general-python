from tkinter import *
from tkinter import ttk
import tkinter as tk
root = Tk()
root.geometry("600x300")
root.title("Quadratic Equation Solver")

x1 = ''
x2 = ''

def calc():
    a = coeff1_value.get()
    b = coeff2_value.get()
    c = coeff3_value.get()
    x1 = (-(int(b))+(((int(b)**2 - 4 * int(a) * int(c))))**0.5) / (2 *int(a))
    x2 = (-(int(b))-(((int(b)**2 - 4 * int(a) * int(c))))**0.5) / (2 *int(a))
    label = Label(root, text= f"Solutions of your quadratic equation are\n {x1}\n{x2}")
    label.grid(columnspan=15, row=7, sticky=tk.N, padx=5, pady=5) 
    pass

# coefficient pf x square
coeff1 = ttk.Label(root, text="Coefficient of x sqaure:")
coeff1.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)

coeff1_value = ttk.Entry(root)
coeff1_value.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)

# coefficient of x
coeff2 = ttk.Label(root, text="Coefficient of x:")
coeff2.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)

coeff2_value = ttk.Entry(root)
coeff2_value.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)

#value of constant

coeff3 = ttk.Label(root,text="Value of constant:")
coeff3.grid(column=0,row=2,sticky=tk.W,padx=5,pady=5)

coeff3_value = ttk.Entry(root)
coeff3_value.grid(column=1,row=2,sticky=tk.E,padx=5,pady=5)

#solution
Solution = ttk.Button(root, text="Get Solution",command=calc)
Solution.grid(column=1, row=5, sticky=tk.W, padx=5, pady=5)


root.mainloop()