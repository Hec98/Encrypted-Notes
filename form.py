from tkinter import Label, Entry, StringVar, Button, Radiobutton
from tkinter.ttk import Combobox
from datetime import date
from uuid import uuid4
from mongodb import set_data, update_data
from control_table import update_table


def form_main(top_form, frame_form, new, data, table, font_main, en_width, btn_1, btn_2):
    btn_1.config(state='disabled')
    btn_2.config(state='disabled')
    def on_close():
        top_form.destroy()
        btn_1.config(state='active')
        btn_2.config(state='active')

    # StringVar
    id_tem = str()
    
    if not new: # Set StringVar
        id_tem = data['_id']
        

    
    def generate_dictionary():
        data = {
            '_id': str(uuid4()) if new else id_tem
                    }
        # if new: data['_id'] = str(uuid4())
        return data

    def all_fields_filled():
        validate = True if id_tem  else False

        return validate
    
    def save_data():
        full_fields = all_fields_filled()
        val_date = False
        if not full_fields: pass
            #var_message.set('Faltan campos por llenar')
            #lb_message['fg'] = '#980009'
        else: pass
            #val_date = validate_en_date(en_dia.get(), en_mes.get(), en_anio.get())
            #if not val_date:
            #    var_message.set('Fecha no valida')
            #    lb_message['fg'] = '#980009'
            # Mas validaciones
        # full_fields, val_date = True, True
        if full_fields and val_date:
            # var_message.set(f'Registro con folio {en_folio_relacionado.get()} guardado correctamente')              
            # lb_message['fg'] = '#009841'
            data = generate_dictionary()
            if new: set_data(data)
            else:
                update_data(id_tem, data)
                on_close()
            update_table(table)
    
    get_button = Button(frame_form, command=save_data, font=font_main, bg='#00986D', fg='white', text='Guadar Registro' if new else 'Editar Registro')
    get_button.grid(row=14, column=0, columnspan=4, sticky="NSWE")

    top_form.protocol('WM_DELETE_WINDOW', on_close)
