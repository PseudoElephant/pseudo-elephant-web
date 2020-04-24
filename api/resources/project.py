from collections import defaultdict

from flask import request, jsonify
from flask_jwt_extended import fresh_jwt_required
from flask_restful import Resource
from marshmallow import ValidationError

from libs.strings import gettext
from models.project import ProjectModel
from schemas.project import ProjectSchema
import traceback

project_schema = ProjectSchema()
projects_schema = ProjectSchema(many=True)


class ProjectById(Resource):
    @classmethod
    def get(cls, _id):
        project = ProjectModel.get_by_id(_id)

        if not project:
            return {"message": gettext("PROJECT_NOT_FOUND").format(_id)}, 404

        return project.json(), 200


class ProjectByTitle(Resource):
    @classmethod
    def get(cls, title):
        project = ProjectModel.get_by_title(title)

        if not project:
            return {"message": gettext("PROJECT_NOT_FOUND").format(title)}, 404

        return project_schema.dump(project), 200

    @classmethod
    @fresh_jwt_required
    def post(cls, title):

        if ProjectModel.get_by_title(title):
            return {"message": gettext("PROJECT_WITH_NAME_EXISTS").format(title)}, 400

        try:
            project_json = request.get_json()

            project = project_schema.load(project_json)

            # they have to send the other attributes (content, desc)
            project.title = title

            project.save_to_mongo()

            return project_schema.dump(project), 201

        except ValidationError as err:
            return err.messages, 400
        except TypeError:
            return {"message": gettext("PROJECT_ERROR_INSERTING")}, 500
        except Exception:
            return {"message": gettext("UNKNOWN_ERROR")}, 500

    @classmethod
    @fresh_jwt_required
    def delete(cls, title):
        project = ProjectModel.get_by_title(title)

        if project:
            project.remove_from_mongo()
        return {"message": gettext("PROJECT_REMOVED").format(title)}, 200

    @classmethod
    @fresh_jwt_required
    def put(cls, title):
        project = ProjectModel.get_by_title(title)

        try:
            # validation of data
            project_json = request.get_json()
            project_new = project_schema.load(project_json)

        except ValidationError as err:
            return err.messages, 400

        # if project exists update
        if project:
            project.content = project_new.content
            project.description = project_new.description

        # create a new one
        else:
            project_new.title = title
            project = project_new

        # saves to db
        try:
            project.save_to_mongo()
            return project_schema.dump(project), 201
        except TypeError:
            print(traceback.print_exc())
            return {"message": gettext("PROJECT_ERROR_INSERTING")}, 500
        except Exception:
            return {"message": gettext("UNKNOWN_ERROR")}, 500


class ProjectList(Resource):
    @classmethod
    def get(cls):
        return {"projects": projects_schema.dump(ProjectModel.all())}
