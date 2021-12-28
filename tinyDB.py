from tinydb import TinyDB, Query
from datetime import datetime

def databaseSelect(name):
    # db = TinyDB(f'db/{name}.json', indent=2, separators=(',', ': '))
    db = TinyDB(f'db/{name}.json', separators=(',', ':'))
    db.default_table_name = f'{name}'
    Element = Query()

    return db, Element

def savePublicKey(n,e):
    data = {
        'parts': { 'n': n, 'e': e },
        'date': datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    }

    db, _ = databaseSelect('public')
    db.insert(data)

def savePrivateKey(n,e, d, p, q):
    data = {
        'parts': { 'n': n, 'e': e, 'd': d, 'p': p, 'q': q },
        'date': datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    }

    db, _ = databaseSelect('private')
    db.insert(data)

def getKeys():
    publicKey, privateKey = [], []

    db, _ = databaseSelect('public')
    for item in db:
        publicKey.append(item['parts']['n'])
        publicKey.append(item['parts']['e'])

    db, _ = databaseSelect('private')
    for item in db:
        privateKey.append(item['parts']['n'])
        privateKey.append(item['parts']['e'])
        privateKey.append(item['parts']['d'])
        privateKey.append(item['parts']['p'])
        privateKey.append(item['parts']['q'])

    return publicKey, privateKey
