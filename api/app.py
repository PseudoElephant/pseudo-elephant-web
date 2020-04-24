import time

from flask import Flask
from flask_jwt_extended import JWTManager
from flask_restful import Api

import os
from dotenv import load_dotenv

from commons.db import Database
from db import mongo
from libs.strings import gettext
from resources.auth import Auth
from resources.blog import BlogByTitle, Blogs
from resources.comment import CommentsByBlog, CommentsQueryByBlog
from resources.project import ProjectByTitle, ProjectList

app = Flask(__name__, static_folder="../build", static_url_path="/")

# Loads enviornment vars

load_dotenv(".env")
environment_configuration = os.environ["CONFIGURATION_SETUP"]
app.config.from_object(environment_configuration)
api = Api(app)
# jwt = JWT(app, authentication_handler=authenticate, identity_handler=identity)  # creates /auth

"""
JWT CONFIGURATION
"""

jwt = JWTManager(app)


@jwt.user_claims_loader
def add_claims_to_jwt(identity):
    pass  # if you want different user with different properties


# Then you should do inside a jwt_required endpoint
# get_jwt_claim() and check if 'is_admin' or what not
# we can have jwt_optional with get_jwt_identity


@jwt.expired_token_loader
def expired_token_callback():
    return {"description": gettext("JWT_EXPIRED_TOKEN"), "error": "expired_token", }, 401


@jwt.invalid_token_loader
def invalid_token_callback(error):
    return {"description": gettext("JWT_INVALID_TOKEN"), "error": "invalid_token", }, 401


@jwt.unauthorized_loader
def unauthorized_callback():
    return (
        {"description": gettext("JWT_UNAUTHORIZED"), "error": "unauthorized_token", },
        401,
    )


@jwt.needs_fresh_token_loader
def needs_fresh_token_callback():
    return (
        {"description": gettext("JWT_NEED_FRESH"), "error": "fresh_token_required", },
        401,
    )


@jwt.revoked_token_loader
def revoked_token_callback():
    return {"description": gettext("JWT_REVOKED"), "error": "token_revoked", }, 401


@app.route("/")
def index():
    return app.send_static_file("index.html")


# Actual API
api.add_resource(Auth, "/auth")
api.add_resource(ProjectByTitle, "/project/title/<string:title>")
api.add_resource(ProjectList, "/projects")
api.add_resource(CommentsByBlog, "/comments/blog_id/<string:blog_id>")
api.add_resource(CommentsQueryByBlog, "/comments/query/<string:blog_id>")
api.add_resource(BlogByTitle, "/blog/<string:title>")
api.add_resource(Blogs,"/blogs")
# could add `/refresh` with TokenRefresh resource


if __name__ == "__main__":
    mongo.init_app(app)
    Database.initialize(mongo.db)
    app.run()

# Improvements :
# Use marshmallow for data validation (more secure)
