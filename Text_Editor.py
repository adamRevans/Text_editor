from tkinter import *
from tkmacosx import Button
from tkinter import scrolledtext
#Existance

# Create Window
root = Tk()
root.title("Buisness Text Editor")

#Window Size
root.geometry("550x350")

#Fun buttons
save_button = Button(root, text='Save')
download_button = Button(root, text='Download Current Text File')
files_button = Button(root, text='Select Text File')

#Text Box
text_area = scrolledtext.ScrolledText(root, width = 70, height = 20,) #Testing

#Placing into Window
text_area.grid(row=2,columnspan=3) #Testing
save_button.grid(row=0, column=0)
download_button.grid(row=0,column=1)
files_button.grid(row=0,column=2)


#Make root work
text_area.focus()#Testing
root.mainloop()