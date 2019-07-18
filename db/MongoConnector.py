from pymongo import MongoClient
import resources.resources as rs
import json
import pandas as pd
import utils.utils as utils
class MongoConnector:

    def __init__(self):
        self.host = rs.MONGO_HOST
        self.port = rs.MONGO_PORT

        self.client = MongoClient(self.host, self.port)
        self.db = self.client.get_database("stocks")


    @property
    def collections(self):
        return self.db.list_collection_names()

    def get_collection_json(self, name):
        data = {}
        collection = self.db.get_collection(name)
        for document in collection.find({}):
            data.update(document)
        del data["_id"]
        return data

    def update_collection(self, name, df):
        new_data = self.df_to_json(df)
        if name in self.collections:
            coll_json = self.get_collection_json(name)
            new_data = utils.combine_dict(new_data,coll_json)
            collection=self.db.get_collection(name)
        else:
            collection = self.db.create_collection(name)

        collection.remove()
        collection.save(new_data)

    def get_collection_df(self,name):
        coll_dict = self.get_collection_json(name)
        # del coll_dict['_id']
        return pd.DataFrame(coll_dict)

    def df_to_json(self,df):
        dfjson = json.loads(df.to_json())
        for x in dfjson.keys():
            dfjson[x] = [dfjson[x][key] for key in dfjson[x].keys()]
        return dfjson
