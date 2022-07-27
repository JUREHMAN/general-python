from tkinter import *
import tkinter as tk
from tkinter import ttk
root = Tk()
root.geometry("600x300")
root.title("My First Login System:")


un = ''
pw = ''
name=''
new_password=''
file_object = open('sample.txt', 'r')
name_value=''
new_password_value=''

def func1():
    un = user_name_value.get()
    pw = password_value.get()
    if un == pw:
        label = Label(root, text= f"You are successfully loged in\nPlease Continue")
        label.grid(columnspan=15, row=7, sticky=tk.N, padx=5, pady=5) 
    else:
        label = Label(root, text= f"Your Username or Password is incorrect\nPlease try again")
        label.grid(columnspan=15, row=7, sticky=tk.N, padx=5, pady=5)

def func2():
    name = Label(root,text="Enter your User Name:")
    name.grid(columnspan=15,row = 9,sticky=tk.N,padx=5,pady=5)

    name_value = ttk.Entry(root)
    name_value.grid(column=1,row = 10,sticky=tk.N,padx=5,pady=5)
    

    new_password = Label(root,text="Enter your New Password here:")
    new_password.grid(columnspan=15,row = 11,sticky=tk.N,padx=5,pady=5)
    
    new_password_value = ttk.Entry(root)
    new_password_value.grid(column=1,row = 12,sticky = tk.N,padx=5,pady=5)
    


    def func3():
        with open ("sample.txt","a") as f:
         f.write(new_password_value.get())
         f.write("\n")
         f.write(name_value.get())
         f.write("\n")
         f.close()
    
    done = ttk.Button(root,text="Done",command=func3)
    done.grid(column = 3, row = 15,sticky = tk.N,padx=5,pady=5)


file_object.close()


#User Name
user_name = ttk.Label(root,text="User Name:")
user_name.grid(column=0,row=0,sticky=tk.W,padx=5,pady=5)

user_name_value = ttk.Entry(root)
user_name_value.grid(column=1,row=0,sticky = tk.E,padx=5,pady=5)

password = ttk.Label(root,text="Password:")
password.grid(column=0,row=1,sticky=tk.W,padx=5,pady=5)

password_value = ttk.Entry(root)
password_value.grid(column=1,row=1,sticky=tk.E,padx=5,pady=5)

#login button
login = ttk.Button(root,text="Login",command=func1)
login.grid(column = 5,row = 4,sticky = tk.N,padx=5,pady=5)

#Signup button

signup = ttk.Button(root,text="Sign Up",command=func2)
signup.grid(column = 5, row = 5,sticky = tk.N,padx=5,pady=5)

root.mainloop()