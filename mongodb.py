from pymongo import MongoClient
from mongoUri import URI

MONGO_URI = URI()
collection = lambda MONGO_URI: MongoClient(MONGO_URI)['notes']['notes']

set_data = lambda data: collection(MONGO_URI).insert_one(data)
get_data = lambda: collection(MONGO_URI).find({'available': True}) 
get_data_one = lambda id_data: collection(MONGO_URI).find_one({'_id': id_data})
remove_data = lambda id_data: collection(MONGO_URI).update_one({'_id': id_data}, {'$set': {'available': False}})
update_data = lambda id_data, data: collection(MONGO_URI).update_one({'_id': id_data}, {'$set': data})
delete_db = lambda: collection(MONGO_URI).delete_many({})
count_db = lambda: collection(MONGO_URI).count_documents({'available': True})
