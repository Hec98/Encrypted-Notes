from tkinter import Tk, Label,LabelFrame, Button
from PIL import Image, ImageTk

from encryption import generateKeys
from topWindows import newNote, getTable

def main_window():
    root = Tk()
    root.title('Encrypted Notes')
    root.geometry('450x220')
    root.resizable(False, False)

    Frame = LabelFrame(root, borderwidth=0, pady=20, padx=20)
    Frame.grid(row=0, column=0)

    # logo
    logo = Image.open('img/logo.png')
    logo = ImageTk.PhotoImage(logo)
    logo_label = Label(Frame, image=logo)
    logo_label['image'] = logo
    logo_label.grid(row=0, column=0)

    frame_button = LabelFrame(root, borderwidth = 0, pady=10, padx=20)

    frame_button.grid(row = 1, column = 0, sticky="N")
    btnNewKeys = Button(frame_button, text='Generate keys', command=generateKeys, font='Source_Code_Pro', bg='#002598', fg='white', height=1, width=10, padx=15)
    btnNewKeys.grid(row=0, column=0)

    btnNewNote = Button(frame_button, text='New None', command=newNote, font='Source_Code_Pro', bg='#00986D', fg='white', height=1, width=10, padx=15)
    btnNewNote.grid(row=0, column=1)

    btnViewNotes = Button(frame_button, text='View Notes', command=getTable, font='Source_Code_Pro', bg='#980009', fg='white', height=1, width=10, padx=15)
    btnViewNotes.grid(row=0, column=2)

    root.mainloop()
