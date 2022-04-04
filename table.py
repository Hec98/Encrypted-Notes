from tkinter import Scrollbar
from tkinter.ttk import Treeview, Style

def control_area(frame, font_main, font_bold, x, y):
    style = Style()
    style.configure('mystyle.Treeview', highlightthickness=0, bd=0, font=font_main) # Modify the font of the body
    style.configure('mystyle.Treeview.Heading', font=font_bold) # Modify the font of the headings
    style.layout('mystyle.Treeview', [('mystyle.Treeview.treearea', {'sticky': 'nswe'})]) # Remove the borders
    
    table_tree = Treeview(frame, selectmode="extended", style='mystyle.Treeview', height=round(y/30))

    scroll_bar = Scrollbar(frame, orient='vertical')
    scroll_bar.grid(row=0, column=1, sticky='NS')
    table_tree.config(yscrollcommand=scroll_bar.set)
    scroll_bar.config(command=table_tree.yview)

    col = table_tree['columns'] = ('id', 'Title', 'Description', 'Link', 'Date')

    width_x = round(x / (len(col) - 1) ) - 8
    col_ra = round(width_x/3)

    table_tree.column("#0", width=0,  stretch="NO")
    table_tree.column(col[0], width=0, stretch="NO")
    table_tree.column(col[1], width=width_x + col_ra, anchor='center')
    table_tree.column(col[2], width=width_x - col_ra, anchor='center')
    table_tree.column(col[3], width=width_x + col_ra, anchor='center')
    table_tree.column(col[4], width=width_x - col_ra, anchor='center')

    table_tree.heading("#0", text='')
    table_tree.heading(col[1], text=col[1])
    table_tree.heading(col[2], text=col[2])
    table_tree.heading(col[3], text=col[3])
    table_tree.heading(col[4], text=col[4])
    table_tree.grid(row=0, column=0, sticky='N')
    return table_tree
