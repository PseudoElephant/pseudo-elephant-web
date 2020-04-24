import traceback

from flask import request
from flask_jwt_extended import fresh_jwt_required
from flask_restful import Resource
from marshmallow import ValidationError

from libs.strings import gettext
from models.blog import BlogModel
from schemas.blog import BlogSchema

blog_schema = BlogSchema()
blogs_schema = BlogSchema(many=True)


class BlogByTitle(Resource):
    @classmethod
    def get(cls, title):
        blog = BlogModel.get_by_title(title)
        if not blog:
            return {"message": gettext("BLOG_NOT_FOUND")}, 404
        return blog_schema.dump(blog), 200

    @classmethod
    @fresh_jwt_required
    def post(cls, title):
        blog = BlogModel.get_by_title(title)
        if blog:
            return {"message": gettext("BLOG_ALREADY_EXISTS").format(title)}
        try:
            blog = blog_schema.load(request.get_json())
            # Update title TODO: think abt this
            blog.title = title
            blog.save_to_mongo()

            return blog_schema.dump(blog), 201
        except ValidationError as err:
            return err.messages, 400
        except TypeError:
            return {"message": gettext("PROJECT_ERROR_INSERTING")}, 500
        except Exception:
            return {"message": gettext("UNKNOWN_ERROR")}, 500

    # improve put
    @classmethod
    @fresh_jwt_required
    def put(cls, title):
        blog = BlogModel.get_by_title(title)

        try:
            # validation of data
            blog_json = request.get_json()
            blog_new = blog_schema.load(blog_json)

        except ValidationError as err:
            return err.messages, 400

        # if project exists update
        if blog:
            blog.content = blog_new.content
            blog.description = blog_new.description
            blog.brief = blog_new.brief

        # create a new one
        else:
            blog_new.title = title
            blog = blog_new

        # saves to db
        try:
            blog.save_to_mongo()
            return blog_schema.dump(blog), 201
        except TypeError:
            print(traceback.print_exc())
            return {"message": gettext("BLOG_ERROR_INSERTING")}, 500
        except Exception:
            return {"message": gettext("UNKNOWN_ERROR")}, 500

    @classmethod
    @fresh_jwt_required
    def delete(cls, title):
        blog = BlogModel.get_by_title(title)

        if blog:
            blog.remove_from_mongo()
        return {"message": gettext("BLOG_REMOVED").format(title)}, 200


# verify
class Blogs(Resource):
    @classmethod
    def get(cls):
        return {"blogs": blogs_schema.dump(BlogModel.all())}
