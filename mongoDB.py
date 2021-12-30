from pymongo import MongoClient
from uuid import uuid4
from datetime import datetime

MONGO_URI = 'mongodb://localhost'

def runMongo(MONGO_URI):
    client = MongoClient(MONGO_URI)
    db = client['notes']
    collection = db['notes']
    return collection

def getDic(type, title, description, link):
    data = {}
    if type is True:
        data = {
            '_id': str(uuid4()),
            'note': {'title': title, 'description': description, 'link': link},
            'available': True,
            'date': datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        }
    else: 
        data = {
            'note': {'title': title, 'description': description, 'link': link},
            'date': datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        }
    return data

def saveDatabase(title, description, link):
    collection = runMongo(MONGO_URI)
    data = getDic(True, title, description, link)
    collection.insert_one(data)

def getData():
    collection = runMongo(MONGO_URI)
    results = collection.find({'available': True})    
    return results

def getDataOne(id):
    collection =  runMongo(MONGO_URI)
    result = collection.find_one({'_id': id})
    return result

def removeData(id):
    collection =  runMongo(MONGO_URI)
    collection.update_one({'_id': id}, {'$set': {'available': False}})

def updateData(id, title, description, link):
    collection =  runMongo(MONGO_URI)
    data = getDic(False, title, description, link)
    collection.update_one({'_id': id}, {'$set': data})

def deleteDB():
    collection = runMongo(MONGO_URI)
    collection.delete_many({})
