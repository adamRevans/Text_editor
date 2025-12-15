from tkinter import *
from tkmacosx import Button
#Existance

# Create Window
root = Tk()
root.title("Buisness Text Editor")

#Window Size
root.geometry("500x500")

#Fun buttons
save_button = Button(root, text='Save')
download_button = Button(root, text='Download Current Text File')
files_button = Button(root, text='Select Text File')

#Text Box
writing_here = Text(root)

#Placing into Window
save_button.grid(row=0, column=0)
download_button.grid(row=0,column=1)
files_button.grid(row=0,column=2)

writing_here.grid(row=1,columnspan=3)


root.mainloop()
