from pymongo import MongoClient
from uuid import uuid4
from datetime import datetime

MONGO_URI = 'mongodb://localhost'

def runMongo(MONGO_URI):
    client = MongoClient(MONGO_URI)
    db = client['notes']
    collection = db['notes']
    return collection

def saveDatabase(title, description, link):
    collection = runMongo(MONGO_URI)

    data = {
        '_id': str(uuid4()),
        'note': {'title': title, 'description': description, 'link': link},
        'date': datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    }

    collection.insert_one(data)

def deleteDB():
    collection = runMongo(MONGO_URI)
    collection.delete_many({})

