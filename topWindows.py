from tkinter import Toplevel, Label, Entry, Button, messagebox, LabelFrame, StringVar
from tkinter.messagebox import showwarning
from tkinter.ttk import Combobox, Treeview, Style

from uuid import uuid4, uuid1
from datetime import datetime

from db import saveNote

def newNote():
    top = Toplevel()
    top.title('New Note')

    lbTitle = Label(top, text='Title: ', font=('Source_Code_Pro',11))
    lbTitle.grid(row=0, column=0)
    enTitle = Entry(top, width=40, font=('Source_Code_Pro',11))
    enTitle.grid(row=0, column=1)

    lbDescription = Label(top, text='Description: ', font=('Source_Code_Pro',11))
    lbDescription.grid(row=1, column=0)
    enDescription = Entry(top, width=40, font=('Source_Code_Pro',11))
    enDescription.grid(row=1, column=1)

    lbLink = Label(top, text='Link: ', font=('Source_Code_Pro',11))
    lbLink.grid(row=2, column=0)
    enLink = Entry(top, width=40, font=('Source_Code_Pro',11))
    enLink.grid(row=2, column=1)

    def save():
        if not enTitle.get() or not enDescription.get() or not enLink.get():
            showwarning('Attention', 'Missing fields to fill')
        else:
            saveNote(enTitle.get(), enDescription.get(), enLink.get())

        top.destroy()
    
    bntSave = Button(top, text='Save', bg='#00FF14', fg='white', font=('Arial',11), command=save)
    bntSave.grid(row=6, column=0, columnspan=2, sticky='we')

    top.mainloop()
