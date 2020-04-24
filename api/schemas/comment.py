from typing import Union, List

from marshmallow import Schema, fields, post_load, validate, ValidationError
from marshmallow.validate import Length

from libs.strings import gettext
from models.comment import CommentModel


class CommentsSchema(Schema):
    class Meta:
        dump_only = ("time_created",)

    title = fields.Str(required=True, validate=Length(max=100))
    content = fields.Str(required=True)
    time_created = fields.Float()

    @post_load
    def make_project(self, *args, **kwargs) -> Union[List, "CommentModel", None]:
        if not kwargs['many']:
            return CommentModel(blog_id="", **args[0])
        else:
            # method for loading multiple comments from json (currently not required)
            pass


class CommentQuerySchema(Schema):
    query = fields.Dict(keys=fields.Str(required=True),
                        values=fields.Int(validate=validate.Range(min=1, max_inclusive=True, max=240,
                                                                  error=gettext("QUERY_VALIDATION_ERROR").format(1,
                                                                                                                 240))),
                        validate=[validate.Length(equal=1),
                                  validate.ContainsOnly([CommentModel.RECENT, CommentModel.LAST_NH])],
                        required=True)


if __name__ == '__main__':
    com_schema = CommentQuerySchema()
    cm_json = com_schema.load({"query": {"last_nh": 2}})
    print(cm_json)
