from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError


class MongoDriver(object):
    host = None
    port = None
    client = None

    def __init__(self, host='localhost', port=27017):
        self.host = host
        self.port = port
        self.client = MongoClient(self.host, self.port)

    def get_database(self, db_name, user_name = None, password = None):
        db = self.client[db_name]
        if user_name == None and password == None: 
            return db
        else:
            if db.authenticate(user_name, password):
                return db
            return None
        

    def get_collection(self, db_name, collection_name):
        return db_name[collection_name]

    def insert_documents(self, collection_name, documents):
        result = None
        try:
            result = collection_name.insert(documents,check_keys=False)
        except DuplicateKeyError:
            print (DuplicateKeyError.message)
        except BulkWriteError:
            print (BulkWriteError.message)
        return result

    def find_document(self, collection_name, filters=None):
        return collection_name.find_one(filters)

    def find_documents(self, collection_name, filters=None, projection=None):
        return collection_name.find(filters, projection)

    def update_document(self, collection_name, obj_id, document):
        return collection_name.find_one_and_update(obj_id, document)

    def close_connection(self):
        return self.client.close()
