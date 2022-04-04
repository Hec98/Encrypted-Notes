from tkinter import Tk, Label,LabelFrame, Button
from PIL import Image, ImageTk

from table import control_area
from control_table import update_table
from buttons import buttons_area

from encryption import generate_keys
# from topWindows import newNote, getTable
from get_resolution import get_resolution

(r_x, r_y) = get_resolution()
font_main, font_bold, font_button, font_form = ('NunitoSans', 10), ('Rubik', 10), ('Rubik', 10), ('OpenSans', 10)

def main_window():
    root = Tk()
    root.title('Encrypted Notes')
    root.geometry(f'{r_x}x{r_y}')
    root.resizable(False, False)

    frame_logo = LabelFrame(root, borderwidth=0, pady=10, padx=10)
    frame_table = LabelFrame(root, borderwidth=0, pady=10, padx=10)
    frame_buttons = LabelFrame(root, borderwidth=0, pady=10, padx=10)
   
    frame_logo.grid(row=0, column=0, sticky="N")
    frame_table.grid(row=1, column=0, sticky="N")
    frame_buttons.grid(row=2, column=0, sticky="N")

    # logo
    logo = Image.open('img/logo.png')
    logo = ImageTk.PhotoImage(logo)
    logo_label = Label(frame_logo, image=logo)
    logo_label.grid(row=0, column=0)

    table = control_area(frame_table, font_main, font_bold, r_x, r_y)

    # update_table(table)
    buttons_area(frame_buttons, table, font_form, font_button, r_x)
    # frame_button = LabelFrame(root, borderwidth = 0, pady=10, padx=20)
 
    # frame_button.grid(row = 1, column = 0, sticky="N")
    # btnNewKeys = Button(frame_button, text='Generate keys', command=generateKeys, font='Source_Code_Pro', bg='#002598', fg='white', height=1, width=10, padx=15)
    # btnNewKeys.grid(row=0, column=0)
 
    # btnNewNote = Button(frame_button, text='New None', command=newNote, font='Source_Code_Pro', bg='#00986D', fg='white', height=1, width=10, padx=15)
    # btnNewNote.grid(row=0, column=1)
 
    # btnViewNotes = Button(frame_button, text='View Notes', command=getTable, font='Source_Code_Pro', bg='#980009', fg='white', height=1, width=10, padx=15)
    # btnViewNotes.grid(row=0, column=2)

    root.mainloop()
