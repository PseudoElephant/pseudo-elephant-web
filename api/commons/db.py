"""
Database logic in one place
"""

import time
from typing import Dict

import pymongo
from db import mongo


class Database(object):
    # URI = "mongodb://localhost:27017"
    # DB_NAME = 'PseudoElephant'
    DATABASE: pymongo.MongoClient = None

    @classmethod
    def initialize(cls, database):
        """
        Starts the database
        """
        # client = pymongo.MongoClient(cls.URI)
        # cls.DATABASE = client[cls.DB_NAME]
        cls.DATABASE = database

    @classmethod
    def insert(cls, collection: str, data: Dict):
        """
        Inserts to collection
        """
        cls.DATABASE[collection].insert(data)

    @classmethod
    def find(cls, collection: str, query: Dict):
        """
        Finds all occurrences
        """
        res = cls.DATABASE[collection].find(query)
        if res is None:
            return None
        else:
            return res

    @classmethod
    def find_one(cls, collection: str, query: Dict):
        """
        Finds one
        """
        res = cls.DATABASE[collection].find_one(query)
        if res is None:
            return None
        else:
            return res

    @classmethod
    def delete_one(cls, collection: str, query: Dict):
        """
        Deletes one based on query
        """
        cls.DATABASE[collection].delete_one(query)

    @classmethod
    def delete_many(cls, collection: str, query: Dict):
        """
        Deletes many based on query
        """
        cls.DATABASE[collection].delete_many(query)

    @classmethod
    def delete_collection_data(cls, collection: str):
        """
        Deletes all content from collection
        """
        cls.DATABASE[collection].delete_many({})

    @classmethod
    def update(cls, collection: str, query: Dict, data: Dict):
        """
         Updates database by value
        """
        cls.DATABASE[collection].update(query, data, upsert=True)

    @classmethod
    def remove(cls, collection):
        cls.DATABASE[collection].remove()


if __name__ == "__main__":
    cl = pymongo.MongoClient("mongodb://localhost:27017")
    # Database.initialize()
    dx = cl["PseudoElephant"]
    # pipeline = [
    #     {
    #         "$project":
    #             {
    #                 "time_created": 1,
    #                 "title": 1,
    #                 "last_tf": {"$gt": ["$time_created", time.time()]},
    #                 "_id": 0
    #             }
    #     }
    # ]
    # res = Database.DATABASE['comments'].aggregate(pipeline=pipeline, cursor={"batchSize": 10})
    # res2 = Database.DATABASE['comments'].find({"time_created": {"$gt": 20}}).sort("time_created", 1).where(
    #     'function() { return this.title == "nice"}')
    # print(list(res))
    # print(list(res2))

    print(dx.comments.delete_one({"x": 1}))
    # res = dx["comments"].remove({'title': "The Big One"})
    # print(res)
    # print(db.list_collection_names())
    # # posts = list(db['posts'].find_one({}))
    # poems = db['poems'].find_one({'user': 'user'})
    # db['poems'].delete_many({})
    # db['posts'].delete_many({})
    #
    # # print("Posts: ")
    # # print(posts)
    #
    # print("Poems: ")
    # print(poems)
