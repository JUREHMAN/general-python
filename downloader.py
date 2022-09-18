'''
It is a simple python programe for youtube video downloading.
Kindly Enter the Valid video URL as this programme can't give you any 
Error/output for invalid or empty URL.
'''
# importing two python libraries
from ssl import ALERT_DESCRIPTION_BAD_CERTIFICATE_HASH_VALUE
from tkinter import *
import tkinter as tk
from tkinter import ttk
from turtle import color
from pytube import YouTube

#GUI setup
root = Tk()
root.title('YouTube DownLoader')
root.geometry('500x300')
root.resizable(0,0)
root.configure(bg='blue')
welcome_label = ttk.Label(root, text="Welcome To YouTube Downloader")
welcome_label.grid(row=2,columnspan=10,padx=100,pady=25)

#U.R.L
url=StringVar()
url_label = ttk.Label(root, text="Kindly paste the URL of the youtube video below")
url_label.grid(row=18,columnspan=10,padx=25,pady=25)

url_entry = ttk.Entry(root,textvariable = url)
url_entry.grid(columnspan=100, row=19, padx=25, pady=0)

#Download Function
def func1():
    url1 =YouTube(str(url_entry.get()))
    video = url1.streams.first()
    video.download(r'/home/junaid/Videos')
    label=Label(root, text = 'Download Complete')
    label.grid(columnspan=100,row=33,padx=75,pady=10)
#Download BUtton
download_button = ttk.Button(root,text="Start Download",command=func1)
download_button.grid(row = 30,padx=175,pady=40)

root.mainloop()