import uuid
from abc import ABCMeta, abstractmethod, abstractclassmethod

# will hook abstract classes to subclasses
from typing import Dict, List, TypeVar, Type, Union

from commons.db import Database

T = TypeVar("T", bound="Model")


class Model(metaclass=ABCMeta):
    """
Model Base Class
Class should not be instanced
    """

    collection: str

    def __init__(self, _id, *args, **kwargs):
        self._id = _id or uuid.uuid4().hex

    @classmethod
    def __new__(cls, *args, **kwargs):
        obj = super(Model, cls).__new__(cls)
        obj._from_base_class = type(obj) == Model

        if not hasattr(args[0], "collection"):
            # Object should have collection attribute
            raise AttributeError(
                f"Objects {args[0]} needs to have class attribute 'collection' "
            )

        return obj

    @abstractmethod
    def json(self) -> Dict:
        """JSON Representation of the class"""
        raise NotImplementedError

    def save_to_mongo(self) -> None:
        """Saves/Updates object in database"""
        Database.update(self.collection, {"_id": self._id}, self.json())

    def remove_from_mongo(self):
        """Removes object from database"""

        Database.delete_one(self.collection, {"_id": self._id})

    @classmethod
    def find_one(cls: Type[T], attribute: str, value: Union[str, Dict]) -> T:
        """Finds one object with given query"""
        obj = Database.find_one(cls.collection, {attribute: value})
        if obj:
            return cls(**obj)

    @classmethod
    def find_many(cls: Type[T], attribute: str, value: str) -> List[T]:
        """Finds many objects with given query"""
        obj = Database.find(cls.collection, {attribute: value})
        return [cls(**elem) for elem in obj]

    @classmethod
    def all(cls: Type[T]) -> List[T]:
        """Finds all objects inside collection"""
        return [cls(**elem) for elem in Database.find(cls.collection, {})]

    @classmethod
    def get_by_id(cls: Type[T], _id: str) -> T:
        """Finds by id the object"""
        json = Database.find_one(cls.collection, {"_id": _id})
        if json:
            return cls(**json)
