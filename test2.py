from tkinter import *

# creating an object of class Tk()
window = Tk()

# change window title
window.title("Hello World")

# change/giving fixed size to window
window.geometry("600x400") # 600 = width & 400 = height

# change the window icon, the icon should be of .ico file
window.iconbitmap("./icon.ico")

#! widgets

# adding a sample label
lb = Label(window, text="Hello world!")
lb.pack()

# adding a textbox
tb = Entry(window)
tb.pack()

# adding a button
btn = Button(window, text="Click Me")
btn.pack()

# mainloop is used to  run the window/tinker 
window.mainloop()