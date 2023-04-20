from tkinter import *

# creating an object of class Tk()
window = Tk()

# change window title
window.title("MilanSony")

# change/giving fixed size to window
window.geometry("600x400") # 600 = width & 400 = height

# disable resizing of window
window.resizable(False, False) #  1st False - width, 2nd False - height

# mainloop is used to  run the window/tinker 
window.mainloop()