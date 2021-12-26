from tkinter import Tk, Canvas, Label,LabelFrame, Button
from PIL import Image, ImageTk

from encryption import generateKeys

def main_window():
    root = Tk()
    root.title('Encrypted Notes')

    canvas = Canvas(root, width=500, height=250)
    canvas.grid(columnspan=3, rowspan=3)

    # logo
    logo = Image.open('img/logo.png')
    logo = ImageTk.PhotoImage(logo)
    logo_label = Label(image=logo)
    logo_label['image'] = logo
    logo_label.grid(row=0, column=1)
        
    frame_button = LabelFrame(root, borderwidth = 0, pady=40)
    frame_button.grid(row = 1, column = 1, sticky="N")

    btn_new = Button(frame_button, text='Generate keys', command=generateKeys, font='Source_Code_Pro', bg='#0005FF', fg='white', height=1, width=10, padx=15)
    btn_new.grid(row=0, column=0)

    root.mainloop()
