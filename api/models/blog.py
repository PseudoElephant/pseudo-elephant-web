"""
Blog Logic
"""
from typing import Dict

from models.base import Model
import uuid
from commons.db import Database
import time


class BlogModel(Model):
    collection = "blogs"

    def __init__(
            self, admin_id: str, title: str, brief: str, content: str, _id: str = None, time_created=time.time()
    ):
        super().__init__(_id)
        self.admin_id = admin_id  # check if valid
        self.title = title
        self.brief = brief
        self.content = content
        self.time_created = time_created

    def json(self) -> Dict:
        return {
            "title": self.title,
            "brief": self.brief,
            "content": self.content,
            "admin_id": self.admin_id,
            "time_created": self.time_created,
        }

    @classmethod
    def get_by_title(cls, title):
        """
        Gets by title
        """
        res = Database.find_one(cls.collection, {"title": title})
        if res:
            return cls(**res)

    @classmethod
    def get_n_recent(cls, n):
        """
        Gets the n recent projects (later could add pagination)
        """
        Database.find(cls.collection, {}).sort({"time_created": {"$gt": 20}}).limit(n)
