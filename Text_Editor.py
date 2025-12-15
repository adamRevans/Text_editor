from tkinter import *
from tkmacosx import Button
#Existance

# Create Window
root = Tk()
root.title("Enter Title Here")

#Window Size
root.geometry("400x400")

#Fun buttons
save_button = Button(root, text='Save')
download_button = Button(root, text='Download Current Text File')
files_button = Button(root, text='Select Text File')

#Text Box
writing_here = Text(root)

#Placing into Window
save_button.grid(row=0, column=0)
