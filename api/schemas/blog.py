from typing import Union

from marshmallow import Schema, fields, post_load, pre_load, ValidationError
from marshmallow.validate import Length

from models.admin import AdminModel
from models.blog import BlogModel


# Maybe add extensions to all values


class BlogSchema(Schema):
    class Meta:
        dump_only = ("_id", "title")
        load_only = ("admin_id",)

    admin_id = fields.Str(required=True)
    title = fields.Str()
    brief = fields.Str(required=True)
    content = fields.Str(required=True)

    @classmethod
    def _verify_admin(cls, data):
        res = AdminModel.get_by_id(data["admin_id"])
        if res is None:
            raise ValidationError("Invalid admin_id.", field_name="Error")

    # _id = String
    @post_load
    def make_project(self, *args, **kwargs) -> Union["BlogModel", None]:
        if not kwargs['many']:
            self._verify_admin(args[0])
            return BlogModel(title="", **args[0])
        else:
            pass
