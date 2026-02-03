from tkinter import *
from tkmacosx import Button
from tkinter import scrolledtext
import random
# ______________________________________
root = Tk()
root.title('HORUS Terminal')
root.geometry('500x500')
# ______________________________________
#demofile.txt can have a different name to make a new file
###WARNING!!! MUST END IN .txt FOR IT TO SAVE PROPERLY!!!GNINRAW###


entry = Entry(root, bg='black', fg='green2', width='50')

TXT= ""
#Definitions
#def xtralyfe():
	#global TXT
	#TXT= entry.get() + ".txt"
	#print(TXT)

def author():
	global TXT
	TXT =  entry.get() + ".txt"
	with open(TXT, 'w') as f:
		f.write(box.get('1.0', END))
		

def printer():
	box.delete('1.0', END) #Source - https://stackoverflow.com/a/27967664 Posted by Fahadkalis Retrieved 2026-02-03, License - CC BY-SA 3.0
	global TXT
	TXT =  entry.get() + ".txt"
	with open(TXT, 'r') as f:
		content = f.read()
		box.insert(END, content)

		

# ______________________________________
#Bits
box = scrolledtext.ScrolledText(root, height='15', width='60', bg='black', fg='green2', font=('bold', 12))
Save = Button(root, text='Save', command=author, bg='black', fg='green2')
Load = Button(root, text='Load', command=printer, bg='black', fg='green2')
#Butt3 = Button(root, text='Save As', bg='black', fg='green2', command=xtralyfe)

# ______________________________________
#Packing
box.grid(row='0', column='0',columnspan='3',rowspan='3')
Save.grid(row='3', column='0')
Load.grid(row='3', column='1')
entry.grid(row='4', column='0', columnspan='3')
#Butt3.grid(row='3',column='2')

# ______________________________________
root.configure(background='dark green')
root.mainloop()
#