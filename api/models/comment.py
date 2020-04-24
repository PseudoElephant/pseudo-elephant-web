"""
Comment Document Class
"""

import time
from typing import Dict

import pymongo

from models.base import Model
from commons.db import Database


class CommentModel(Model):
    RECENT = "recent"
    LAST_NH = "last_nh"
    collection = "comments"

    def __init__(self, blog_id: str, title: str, content: str, _id=None, time_created=time.time()):
        super().__init__(_id)
        self.title = title
        self.content = content
        self.blog_id = blog_id
        self.time_created = time_created

    def json(self) -> Dict:
        return {
            "title": self.title,
            "content": self.content,
            "time_created": self.time_created,
            "blog_id": self.blog_id
        }

    @classmethod
    def get_last_tf(cls, blog_id):
        """
        Will return the last 24h of comments
        """
        one_day = 86400
        res = Database.find(cls.collection, {"time_created": {"$gt": time.time() - one_day}, "blog_id": blog_id})
        if res:
            return [cls(**r) for r in res]

    @classmethod
    def get_last_nh(cls, hr: int, blog_id: str):
        """
        Returns all of the comments from the last n days
        """
        tm = hr * 60 * 60
        res = Database.find(cls.collection, {"time_created": {"$gt": time.time() - tm}, "blog_id": blog_id})
        if res:
            return [cls(**r) for r in res]

    @classmethod
    def get_n_most_recent(cls, n: int, blog_id: str):
        """
        Gets most recent instance
        """
        res = Database.find(cls.collection, {"blog_id": blog_id}).sort("time_created", -1).limit(n)
        if res:
            return [cls(**r) for r in res]

    @classmethod
    def get_all_by_filter_title(cls, blog_id, query):
        """
        Gets all of comments based on filter
        """
        res = Database.find(cls.collection, {"blog_id": blog_id}).where(
            'function() { return this.title == ' + query + ' }'
        )
        if res:
            return [cls(**r) for r in res]

    @classmethod
    def get_all_by_blog_id(cls, blog_id):
        res = Database.find(cls.collection, {"blog_id": blog_id})
        if res:
            return [cls(**r) for r in res]


if __name__ == "__main__":
    cl = pymongo.MongoClient("mongodb://localhost:27017")
    # Database.initialize()
    dx = cl["PseudoElephant"]
    cmt = dx.find("comments", {"time_created": {"$gt": time.time() - 3600, "blog_id": 1}})
    print(cmt)
