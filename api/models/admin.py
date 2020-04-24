"""
Admin model, handles the retrieval of the admins, update and deletion.
"""

from typing import Union, Dict

from security.encrypt import encrypt_password
from commons.db import Database
from models.base import Model


class AdminModel(Model):
    """
    Class only to be used by admins, not visible to normal users.
    """

    collection = "admins"

    def __init__(self, username: str, password: str, _id: str = None, **kwargs):
        super().__init__(_id)
        self.username = username
        if kwargs.get("retrieve"):
            self.password = password
        else:
            self.password = encrypt_password(password)

    @classmethod
    def get_by_username(cls, username: str) -> Union["Admin", None]:
        """
        Get admin by email.
        """
        data = Database.find_one(cls.collection, {"username": username})
        if data is not None:
            return cls(**data, retrieve=True)
        return None

    @classmethod
    def get_by_id(cls, _id: str) -> Union["Admin", None]:
        """
        Get admin by _Id.
        """
        data = Database.find_one(cls.collection, {"_id": _id})
        if data is not None:
            return cls(**data, retrieve=True)
        return None

    def json(self) -> Dict:
        """
        Returns json representation.
        """
        return {"_id": self._id, "username": self.username, "password": self.password}


if __name__ == "__main__":
    """
    Example of the Admin Model
    """
    print("------------TESTING ADMIN MODEL--------------")
    Database.initialize()

    admin = AdminModel("Ale", "pass")
    admin.save_to_mongo()
    # admin.delete_from_mongo()
    # admin = Admin.get_by_username("Steph")
    # print(admin.json)
    # Database.delete_collection_data('admins')
    # print(Admin.validate_admin("Mike", "pass"))
