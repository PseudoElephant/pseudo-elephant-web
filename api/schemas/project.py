from typing import Union

from marshmallow import Schema, fields, post_load
from marshmallow.validate import Length

from models.project import ProjectModel


class ProjectSchema(Schema):
    class Meta:
        dump_only = ("title",)

    fields.Str(required=True, validate=Length(max=100))
    description = fields.Str(required=True)
    content = fields.Str(required=True)

    @post_load
    def make_project(self, *args, **kwargs) -> Union["ProjectModel", None]:
        if not kwargs['many']:
            return ProjectModel(title="", **args[0])
        else:
            # method for loading multiple projects from json (currently not required)
            pass

# Serialization = book to dict
# Deserialization = dict to book
# I can add a @postload method to convert automatically into a model
# Smart hyperlinking with flask-marshmallow
# right now you cant update the title (on purpose)
