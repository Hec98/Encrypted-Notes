from pymongo import MongoClient
from mongo_uri import uri

MONGO_URI = uri()

def run_mongo(MONGO_URI):
    client = MongoClient(MONGO_URI)        
    db = client['h_programas']
    collection = db['programas']
    return collection

def set_data(data):
    collection = run_mongo(MONGO_URI)
    collection.insert_one(data)

def get_data():
    collection = run_mongo(MONGO_URI)
    results = collection.find({'visible': True}) 
    return results

def get_data_one(id_data):
    collection =  run_mongo(MONGO_URI)
    result = collection.find_one({'_id': id_data})
    return result

def remove_data(id_data):
    collection =  run_mongo(MONGO_URI)
    collection.update_one({'_id': id_data}, {'$set': {'visible': False}})

def update_data(id_data, data):
    collection =  run_mongo(MONGO_URI)
    collection.update_one({'_id': id_data}, {'$set': data})

def delete_db():
    collection = run_mongo(MONGO_URI)
    collection.delete_many({})
