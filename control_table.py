from mongodb import get_data, count_db
from encryption import decrypted
from tkinter import Entry, Label, Button

def update_table(table):
    count = count_db()
    print(f'{count} notes stored')
    records = table.get_children()  
    for element in records: table.delete(element)   
    results = get_data() 
    data_table = list()
    tem_count = 1
    for data in results:
        print(f'Note {tem_count} of {count}')
        tem_count+=1
        tem = list()
        tem.append(data['_id'])     
        tem.append(decrypted(data['note']['title']))      
        tem.append(decrypted(data['note']['description']))      
        tem.append(decrypted(data['note']['link']))      
        tem.append(data['date'])
        data_table.append(tuple(tem))
    data_table = tuple(data_table)
    
    for add_table in data_table: table.insert(parent='', index='end', values=(add_table))

def get_id(table):
    try:
        id_data = table.item(table.focus())        
        id_data = id_data['values'][0] if id_data is not None else None
        return id_data
    except: pass

def search(frame_search, table, font_main, font_button, en_width, width_button):
    en_search = Entry(frame_search, width=en_width, font=font_main)
    en_search.grid(row=0, column=0)
    
    lb = Label(frame_search, text='')
    lb.grid(row=0, column=1)

    def search():
        records = table.get_children()  
        for element in records: table.delete(element)
        results = get_data()
        data_table = list()
        for data in results:
            tem = list()
            tem.append(decrypted(data['note']['title']).lower())
            tem.append(decrypted(data['note']['description']).lower())      
            tem.append(decrypted(data['note']['link']).lower())      
            tem.append(data['date'])
            tem_match = list(filter(lambda term: en_search.get().lower() in term, tem))

            tem2 = list()
            tem2.append(data['_id'])     
            tem2.append(decrypted(data['note']['title']))      
            tem2.append(decrypted(data['note']['description']))      
            tem2.append(decrypted(data['note']['link']))      
            tem2.append(data['date'])
            if len(tem_match) > 0: data_table.append(tuple(tem2))

        data_table = tuple(data_table)
        for add_table in data_table: table.insert(parent='', index='end', values=(add_table))
        en_search.delete(0, len(en_search.get()))

    def search_confirm(): search() if len(en_search.get()) > 0 else None
    btn_search = Button(frame_search, text='Search', command=search_confirm, font=font_button, bg='#002598', fg='white', height=1, width=width_button, padx=15)
    btn_search.grid(row=0, column=2)
