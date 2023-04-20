from tkinter import *

# creating an object of class Tk()
window = Tk()

# change window title
window.title("MilanSony")

# change/giving fixed size to window
window.geometry("600x400") # 600 = width & 400 = height

# disable resizing of window
window.resizable(False, False) #  1st False - width, 2nd False - height
# if we give 1st parameter as True and 2nd as False we can adjust the width only, if we give 2nd parameter as True and 1st as False we can adjust the height only

# change the window icon, the icon should be of .ico file
window.iconbitmap("./icon.ico")

# change background color of window
window.configure(bg="#000000")

# mainloop is used to  run the window/tinker 
window.mainloop()