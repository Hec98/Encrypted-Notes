from tinydb import TinyDB, Query
from uuid import uuid4
from datetime import datetime

def databaseSelect(name):
    db = TinyDB(f'db/{name}.json', indent=2, separators=(',', ': '))
    # db = TinyDB(f'db/{name}.json', separators=(',', ':'))
    db.default_table_name = f'{name}'
    Element = Query()

    return db, Element

def savePublicKey(n,e):
    data = {
        'id': str(uuid4()),
        'parts': { 'n': n, 'e': e },
        'date': datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    }

    db, _ = databaseSelect('public')
    db.insert(data)

def savePrivateKey(n,e, d, p, q):
    data = {
        'id': str(uuid4()),
        'parts': { 'n': n, 'e': e, 'd': d, 'p': p, 'q': q },
        'date': datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    }

    db, _ = databaseSelect('private')
    db.insert(data)

def saveNote(title, description, link):
    data = {
        'id': str(uuid4()),
        'note': { 'title': title, 'description': description, 'link': link },
        'completed': False,
        'date': datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    }

    db, _ = databaseSelect('note')
    db.insert(data)

