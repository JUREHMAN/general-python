from tkinter import *
root = Tk()
root.title("Buttons Interface")
root.geometry("1200x1000")
f1 = Frame(root,borderwidth=7,bg="grey",relief=SUNKEN)
f1.pack(side=LEFT,anchor="nw")

def print1():
    print("This is the first statement\n")

def print2():
    print("This is the second statement\n")

def print3():
    print("This is the third statement\n")

def print4():
    print("This is the fourth statement\n")




b1 = Button(f1,fg="red",text="Print Statement 1",command=print1)
b1.pack(side=LEFT)

b2 = Button(f1,fg="red",text="Print Statement 2",command=print2)
b2.pack(side=LEFT)

b3 = Button(f1,fg="red",text="Print Statement 3",command=print3)
b3.pack(side=LEFT)

b4 = Button(f1,fg="red",text="Print Statement 4",command=print4)
b4.pack()

root.mainloop()