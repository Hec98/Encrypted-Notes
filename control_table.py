from mongodb import get_data, count_db
from encryption import decrypted

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
