from tkinter import Label, Entry, StringVar, Button, Radiobutton
from tkinter.ttk import Combobox
from datetime import datetime
from uuid import uuid4
from encryption import encryption, decrypted
from mongodb import set_data, update_data
from control_table import update_table


def form_main(top_form, frame_form, new, data, table, font_main, font_button, en_width, btn_1, btn_2):
    btn_1.config(state='disabled')
    btn_2.config(state='disabled')
    def on_close():
        top_form.destroy()
        btn_1.config(state='active')
        btn_2.config(state='active')

    # StringVar
    id_tem = str()
    var_title = StringVar()
    var_description = StringVar()
    var_link = StringVar()
    var_message = StringVar()
    
    if not new: # Set StringVar
        id_tem = data['_id']
        var_title.set(decrypted(data['note']['title']))
        var_description.set(decrypted(data['note']['description']))
        var_link.set(decrypted(data['note']['link']))
        var_message.set(f"Date: {data['date']}")

        
    lb_title = Label(frame_form, text='Title: ', font=font_main, pady=3, padx=10)
    lb_title.grid(row=0, column=0)
    en_title = Entry(frame_form, textvariable=var_title, width=en_width, font=font_main)
    en_title.focus()
    en_title.grid(row=0, column=1)

    lb_description = Label(frame_form, text='Description: ', font=font_main, pady=3, padx=10)
    lb_description.grid(row=1, column=0)
    en_description = Entry(frame_form, textvariable=var_description, width=en_width, font=font_main)
    en_description.grid(row=1, column=1)

    lb_link = Label(frame_form, text='Link: ', font=font_main, pady=3, padx=10)
    lb_link.grid(row=2, column=0)
    en_link = Entry(frame_form, textvariable=var_link, width=en_width, font=font_main)
    en_link.grid(row=2, column=1)

    lb_message = Label(frame_form, font=('OpenSans', 10, 'bold'), textvariable=var_message)
    lb_message.grid(row=3, column=0, columnspan=4, sticky="NSWE")
    
    def generate_dictionary():
        data = {
            '_id': str(uuid4()) if new else id_tem,
            'note': {'title': encryption(en_title.get()), 'description': encryption(en_description.get()), 'link': encryption(en_link.get())},
            'date': datetime.now().strftime('%d-%m-%Y %H:%M:%S'),
            'available': True
            }
        # if new: data['_id'] = str(uuid4())
        return data

    def all_fields_filled():
        validate = True if en_title.get() and en_description.get() and en_link.get()  else False

        return validate
    
    def save_data():
        full_fields = all_fields_filled()
        # val_date = False
        if not full_fields:
            var_message.set('Faltan campos por llenar')
            lb_message['fg'] = '#980009'
        else: pass
            #val_date = validate_en_date(en_dia.get(), en_mes.get(), en_anio.get())
            #if not val_date:
            #    var_message.set('Fecha no valida')
            #    lb_message['fg'] = '#980009'
            # Mas validaciones
        # full_fields, val_date = True, True
        if full_fields:
            var_message.set(f'The record with title: {en_title.get()} was saved')              
            lb_message['fg'] = '#009841'
            data = generate_dictionary()
            if new: set_data(data)
            else:
                update_data(id_tem, data)
                on_close()
            update_table(table)
    
    get_button = Button(frame_form, command=save_data, font=font_button, bg='#00986D', fg='white', text='Guadar Registro' if new else 'Editar Registro')
    get_button.grid(row=4, column=0, columnspan=4, sticky="NSWE")

    top_form.protocol('WM_DELETE_WINDOW', on_close)
