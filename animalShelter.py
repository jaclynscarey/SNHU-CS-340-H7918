from pymongo import MongoClient

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """
    
    def __init__(self, username, password):        
        host = 'nv-desktop-services.apporto.com'
        port = 32069
        database = 'AAC'

        self.client = MongoClient(f'mongodb://{username}:{password}@{host}:{port}')
        self.database = self.client[database]
        self.collection = self.database['animals']
        print('Connection Successful')

    def create(self, data):
        """ Method to insert a document into a specified collection """
        if data is not None:
            self.database.animals.insert_one(data)  # data should be dictionary
            return True
        else:
            raise Exception("Nothing to save, because data parameter is empty")

    def read(self, query=None):
        """ Method to query documents from a specified collection """
        if query is not None:
            return self.database.animals.find(query)
        else:
            raise Exception("No matching results were found")
            
    def update(self, query, data):
        """Method to update documents from a specified collection"""
        if query and data:
            result = self.database.animals.update_many(query, {"$set": data})
            return result.modified_count
        else:
            return 0

    def delete(self, query):
        """Method to delete a document from a specified collection"""
        if query:
            result = self.database.animals.delete_many(query)
            return result.deleted_count
        else:
            return 0

        
            
            
