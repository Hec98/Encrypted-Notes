from tkinter import Button, Label, Toplevel, LabelFrame
from tkinter.messagebox import askyesno
from encryption import generate_keys
from form import form_main
from mongodb import remove_data, get_data_one
from control_table import update_table, get_id

def buttons_area(frame_button, table, font_form, font_button, x):
    def get_top_form(title):
        top_form = Toplevel()
        top_form.title(title)
        top_form.resizable(False, False)
        frame_form = LabelFrame(top_form, borderwidth=0, pady=20, padx=20)
        frame_form.grid(row=0, column=0, sticky="N")
        return top_form, frame_form

    def get_form():
        top_form, frame_form = get_top_form('Guardar Registro')
        form_main(top_form, frame_form, True, None, table, font_form, font_button, 100, btn_new_record, btn_update)
    
    def edit_data(id_data, edit):
        if id_data is not None:
            if edit:
                data = get_data_one(id_data)
                top_form, frame_form = get_top_form('Editar Registro')
                form_main(top_form, frame_form, False, data, table, font_form, font_button, 100, btn_new_record, btn_update)
            else:
                ask = askyesno('Atención', '¿Desea remover el registro seleccionado?')
                if ask:
                    remove_data(id_data)
                    update_table(table)
     
    width_button = round(x/80)
   
    btn_new_keys = Button(frame_button, text='Generate keys', command=generate_keys, font=font_button, bg='#002598', fg='white', height=1, width=width_button, padx=15)
    btn_new_record = Button(frame_button, text='New Note', command=get_form, font=font_button, bg='#009841', fg='white', height=1, width=width_button, padx=15)
    btn_update = Button(frame_button, text='Edit Note', command=lambda: edit_data(get_id(table), True), bg='#00986D', font=font_button, fg='white', height=1, width=width_button, padx=15)
    btn_delete = Button(frame_button, text='Remove Note', command=lambda: edit_data(get_id(table), False), bg='#980009', font=font_button, fg='white', height=1, width=width_button, padx=15)
    btn_refresh = Button(frame_button, text='Refresh', command=lambda: update_table(table), bg='#008998', font=font_button, fg='white', height=1, width=width_button, padx=15)
  
    empty_space_0 = Label(frame_button, font=font_button, text='')
    empty_space_1 = Label(frame_button, font=font_button, text='')
    empty_space_2 = Label(frame_button, font=font_button, text='')
    empty_space_3 = Label(frame_button, font=font_button, text='')
 
    btn_new_keys.grid(row=0, column=0)
    empty_space_0.grid(row=0, column=1)
    btn_new_record.grid(row=0, column=2)
    empty_space_1.grid(row=0, column=3)
    btn_update.grid(row=0, column=4)       
    empty_space_2.grid(row=0, column=5)
    btn_delete.grid(row=0, column=6)
    empty_space_3.grid(row=0, column=7)
    btn_refresh.grid(row=0, column=8)
