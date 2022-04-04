from pymongo import MongoClient
from mongo_uri import uri

MONGO_URI = uri()

def run_mongo(MONGO_URI):
    client = MongoClient(MONGO_URI)        
    db = client['notes']
    collection = db['notes']
    return collection

def set_data(data):
    collection = run_mongo(MONGO_URI)
    collection.insert_one(data)

def get_data():
    collection = run_mongo(MONGO_URI)
    results = collection.find({'available': True}) 
    return results

def get_data_one(id_data):
    collection =  run_mongo(MONGO_URI)
    result = collection.find_one({'_id': id_data})
    return result

def remove_data(id_data):
    collection =  run_mongo(MONGO_URI)
    collection.update_one({'_id': id_data}, {'$set': {'available': False}})

def update_data(id_data, data):
    collection =  run_mongo(MONGO_URI)
    collection.update_one({'_id': id_data}, {'$set': data})

def delete_db():
    collection = run_mongo(MONGO_URI)
    collection.delete_many({})

def count_db():
    collection = run_mongo(MONGO_URI)
    return collection.count_documents({'available': True})
