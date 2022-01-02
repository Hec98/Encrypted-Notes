from tkinter import Toplevel, Label, Entry, Button, LabelFrame, StringVar
from tkinter.messagebox import showwarning, askyesno
from tkinter.ttk import Treeview, Style

from os.path import isfile

from encryption import encryption, decrypted
from mongoDB import getDataOne, saveDatabase, getData, removeData, updateData

def newNote():
    if not isfile('db/public.json') and not isfile('db/private.json'): showwarning('Attention', 'Generate keys first please')
    else: generateNote()

def getTable():
    if not isfile('db/public.json') and not isfile('db/private.json'): showwarning('Attention', 'Generate keys first please')
    else: generateTable()

def generateNote():
    top = Toplevel()
    top.title('New Note')
    top.resizable(False, False)

    lbTitle = Label(top, text='Title: ', font=('Source_Code_Pro',11))
    lbTitle.grid(row=0, column=0)
    enTitle = Entry(top, width=50, font=('Source_Code_Pro',11))
    enTitle.focus()
    enTitle.grid(row=0, column=1)

    lbDescription = Label(top, text='Description: ', font=('Source_Code_Pro',11))
    lbDescription.grid(row=1, column=0)
    enDescription = Entry(top, width=50, font=('Source_Code_Pro',11))
    enDescription.grid(row=1, column=1)

    lbLink = Label(top, text='Link: ', font=('Source_Code_Pro',11))
    lbLink.grid(row=2, column=0)
    enLink = Entry(top, width=50, font=('Source_Code_Pro',11))
    enLink.grid(row=2, column=1)

    def save():
        if not enTitle.get() or not enDescription.get() or not enLink.get():
            showwarning('Attention', 'Missing fields to fill')
        else:
            title = encryption(enTitle.get())
            description = encryption(enDescription.get())
            link = encryption(enLink.get())
            saveDatabase(title, description, link)

        top.destroy()

    frame_button = LabelFrame(top, borderwidth = 0, pady=5)
    frame_button.grid(row = 3, column = 0, columnspan=2, sticky="N")

    bntSave = Button(frame_button, text='Save', bg='#00986D', fg='white', font=('Source_Code_Pro',11), height=1, width=57, command=save)
    bntSave.grid(row=0, column=0,sticky='we')

    top.mainloop()

def generateTable():
    def get_id():
        try:
            id = table.item(table.focus())
            id = id['values'][0] if id is not None else None
            return id
        except:
            pass

    def updateTable():
        records = table.get_children()
        for element in records: table.delete(element)
        results = getData()

        dataTable = []
        for r in results:
            tem = []
            tem.append(r['_id'])
            tem.append(decrypted(r['note']['title']))
            tem.append(decrypted(r['note']['description']))
            tem.append(decrypted(r['note']['link']))
            tem.append(r['date'])
            dataTable.append(tem)

        for addTable in dataTable: table.insert(parent='', index='end', values=(addTable))

    def edit():
        id = get_id()
        data = getDataOne(id)
        if id is not None: top.destroy()
        try: editRecord(data)
        except: pass

    def remove():
        id = get_id()
        res = askyesno('Warning', 'Are you sure you want to remove this record?')
        if res is True: removeData(id)
        updateTable()

    top = Toplevel()
    top.title('My notes')
    top.resizable(False, False)

    style = Style()
    style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('Source_Code_Pro', 11)) # Modify the font of the body
    style.configure("mystyle.Treeview.Heading", font=('Source_Code_Pro', 12,'bold')) # Modify the font of the headings
    style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})]) # Remove the borders

    table = Treeview(top, style="mystyle.Treeview")

    col = table['columns'] = ('id', 'Title', 'Description', 'Link', 'Date')

    table.column("#0", width=0,  stretch="NO")
    table.column(col[0], width=0, stretch="NO")
    table.column(col[1], width=250, anchor='center')
    table.column(col[2], width=250, anchor='center')
    table.column(col[3], width=300, anchor='center')
    table.column(col[4], width=190, anchor='center')

    table.heading("#0", text='')
    table.heading(col[1], text=col[1])
    table.heading(col[2], text=col[2])
    table.heading(col[3], text=col[3])
    table.heading(col[4], text=col[4])

    table.grid(row=0, column=0)

    frame_button = LabelFrame(top, borderwidth = 0, pady=5)
    frame_button.grid(row = 1, column = 0, sticky="N")

    bnt_update = Button(frame_button, text='Edit', command=edit, bg='#00986D', font='Source_Code_Pro', fg='white', height=1, width=10, padx=15)
    bnt_update.grid(row=0, column=0, sticky='we')
    bnt_delete = Button(frame_button, text='Remove', command=remove, bg='#980009', font='Source_Code_Pro', fg='white', height=1, width=10, padx=15)
    bnt_delete.grid(row=0, column=1, sticky='we')
    updateTable()

    top.mainloop()

def editRecord(data):
    id = data['_id']

    varTitle = StringVar()
    varTitle.set(decrypted(data['note']['title']))
    varDescription = StringVar()
    varDescription.set(decrypted(data['note']['description']))
    varLink = StringVar()
    varLink.set(decrypted(data['note']['link']))

    top = Toplevel()
    top.title('Edit Record')
    top.resizable(False, False)

    lbTitle = Label(top, text='Title: ', font=('Source_Code_Pro',11))
    lbTitle.grid(row=0, column=0)
    enTitle = Entry(top, width=50, textvariable=varTitle, font=('Source_Code_Pro',11))
    enTitle.focus()
    enTitle.grid(row=0, column=1)

    lbDescription = Label(top, text='Description: ', font=('Source_Code_Pro',11))
    lbDescription.grid(row=1, column=0)
    enDescription = Entry(top, width=50, textvariable=varDescription, font=('Source_Code_Pro',11))
    enDescription.grid(row=1, column=1)

    lbLink = Label(top, text='Link: ', font=('Source_Code_Pro',11))
    lbLink.grid(row=2, column=0)
    enLink = Entry(top, width=50, textvariable=varLink, font=('Source_Code_Pro',11))
    enLink.grid(row=2, column=1)

    def save():
        if not enTitle.get() or not enDescription.get() or not enLink.get():
            showwarning('Attention', 'Missing fields to fill')
        else:
            title = encryption(enTitle.get())
            description = encryption(enDescription.get())
            link = encryption(enLink.get())
            updateData(id, title, description, link)
            top.destroy()
            getTable()

    frame_button = LabelFrame(top, borderwidth = 0, pady=5)
    frame_button.grid(row = 5, column = 0, columnspan=2, sticky="N")

    bntSave = Button(frame_button, text='Save', bg='#00986D', fg='white', font=('Source_Code_Pro',11), height=1, width=57, command=save)
    bntSave.grid(row=0, column=0,sticky='we')

    top.mainloop()
