"""
Project Document Class
"""

import time
from typing import Dict, Union, List

from models.base import Model
from commons.db import Database


class ProjectModel(Model):
    collection = "projects"

    def __init__(self, title: str, content: str, description: str, _id=None, **kwargs):
        super().__init__(_id)

        # for retrieval purposes
        if "time_created" in kwargs:
            self.time_created = kwargs["time_created"]
        else:
            self.time_created = time.time()

        self.title = title
        self.description = description
        self.content = content

        # maybe image

    def json(self):
        return {
            "title": self.title,
            "description": self.description,
            "content": self.content,
            "time_created": self.time_created,
        }

    @classmethod
    def get_n_recent(cls, n) -> Union[List, None]:
        """
        Gets the n recent projects
        """
        obj = (
            Database.find(cls.collection, {})
            .sort({"time_created": {"$gt": 20}})
            .limit(n)
        )
        if obj:
            return [cls(**o) for o in obj]

    @classmethod
    def get_by_title(cls, title) -> Union["ProjectModel", None]:
        """
        Gets by title
        """
        obj = Database.find_one(cls.collection, {"title": title})
        if obj:
            return cls(**obj)
