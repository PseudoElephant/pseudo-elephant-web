from flask import request
from flask_restful import Resource
from marshmallow import ValidationError

from libs.strings import gettext
from models.blog import BlogModel
from models.comment import CommentModel
from schemas.comment import CommentsSchema, CommentQuerySchema

comments_schema = CommentsSchema(many=True)
comment_schema = CommentsSchema()
comments_query_schema = CommentQuerySchema(many=True)
comment_query_schema = CommentQuerySchema()


class CommentsByBlog(Resource):
    @classmethod
    def get(cls, blog_id):
        comments = CommentModel.get_all_by_blog_id(blog_id)
        if not comments:
            return {"message": gettext("COMMENTS_NOT_FOUND")}, 404
        return {"comments": comments_schema.dump(comments)}, 200

    @classmethod
    def post(cls, blog_id):
        blog = BlogModel.get_by_id(blog_id)
        if not blog:
            return {"message": gettext("BLOG_NOT_FOUND")}
        try:
            comment = comment_schema.load(request.get_json())

            comment.blog_id = blog_id

            comment.save_to_mongo()

            return comment_schema.dump(comment), 201
        except ValidationError as err:
            return err.messages, 400
        except TypeError:
            return {"message": gettext("PROJECT_ERROR_INSERTING")}, 500
        except Exception:
            return {"message": gettext("UNKNOWN_ERROR")}, 500


class CommentsQueryByBlog(Resource):
    @classmethod
    def post(cls, blog_id):
        try:
            query_json = request.get_json()
            print(query_json)
            payload = comment_query_schema.load(query_json)
        except ValidationError as err:
            return err.messages, 400

        comments = None
        req = None

        payload = payload['query']
        # Gets n most recent
        if CommentModel.RECENT in payload:
            value = payload[CommentModel.RECENT]
            req = CommentModel.RECENT
            comments = CommentModel.get_n_most_recent(value, blog_id=blog_id)

        elif CommentModel.LAST_NH in payload:
            value = payload[CommentModel.LAST_NH]
            req = CommentModel.LAST_NH
            comments = CommentModel.get_last_nh(value, blog_id=blog_id)

        if comments:
            return {"comments": comments_schema.dump(comments),
                    "request": req
                    }, 200
        return {"message": gettext("COMMENTS_NOT_FOUND")}, 404
