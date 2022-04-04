from mongodb import get_data

def update_table(table):
    records = table.get_children()    
    for element in records: table.delete(element)    
    results = get_data()   
    data_table = list()

    for data in results:
        tem = list()
        tem.append(data['_id'])        
        tem.append(data['folio_relacionado'])
        tem.append(f"{data['nombre']['nombre']}\n{data['nombre']['primer_apellido']}\n{data['nombre']['segundo_apellido']}")
        tem.append(f"{data['fecha_nacimiento']['dia']}-{data['fecha_nacimiento']['mes']}-{data['fecha_nacimiento']['anio']}\n{data['sexo']}")
        #tem.append(data['sexo'])
        tem.append(f"{data['claves']['clave_estado_civil']}\n{data['claves']['folio_id_oficial']}")
        #tem.append(data['claves']['clave_grado_estudios'])
        tem.append(data['claves']['folio_id_oficial'])
        tem.append(data['claves']['clave_entidad_nacimiento'])
        tem.append(data['claves']['curp'])
        tem.append(data['programa'])
        tem.append(f"{data['direccion']['calle']}, {data['direccion']['numero_exterior']}, {data['direccion']['numero_interior']}, {data['direccion']['codigo_postal']}, {data['direccion']['colonia']}")
        tem.append(f"{data['telefonos']['telefono']}\n{data['telefonos']['celular']}")
        data_table.append(tuple(tem))
    data_table = tuple(data_table)
    
    for add_table in data_table: table.insert(parent='', index='end', values=(add_table))

def get_id(table):
    try:
        id_data = table.item(table.focus())         
        id_data = id_data['values'][0] if id_data is not None else None
        return id_data
    except: pass
