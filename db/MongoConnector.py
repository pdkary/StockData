from pymongo import MongoClient
import resources.resources as rs


class MongoConnector:

    def __init__(self):
        self.host = rs.MONGO_HOST
        self.port = rs.MONGO_PORT

        self.client = MongoClient(self.host, self.port)

    def test(self):
        print(self.client.fiix.list_collection_names())
