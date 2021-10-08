from tkinter import*
from tkinter.ttk import*
from time import strftime
window=Tk()                   #to create a new tkinter window
window.title("Clock")
label=Label(window,font=("sans",80),background="white",foreground="black")
label.pack(anchor="e")
def time():
    clock=strftime("%H:%M:%S")
    label.config(text=clock)
    label.after(1000,time)
time()
mainloop()