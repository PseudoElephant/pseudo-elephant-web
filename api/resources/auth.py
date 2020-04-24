from flask import request
from flask_jwt_extended import (
    create_access_token,
    jwt_refresh_token_required,
    get_jwt_identity,
    create_refresh_token,
)
from flask_restful import Resource

from libs.strings import gettext
from models.admin import AdminModel
from security.encrypt import check_encrypted_password


class Auth(Resource):
    """
    Handles authorization, creation of jwt tokens
    """

    @classmethod
    def post(cls):
        data = request.get_json()

        # Get admin
        admin = AdminModel.get_by_username(data["username"])

        # authenticate
        if admin and check_encrypted_password(data["password"], admin.password):
            # identity
            access_token = create_access_token(identity=admin._id, fresh=True)
            resfresh_token = create_refresh_token(identity=admin._id)
            return {"access_token": access_token, "refresh_token": resfresh_token}, 200

        return {"message": gettext("AUTH_INVALID_CREDENTIALS")}, 401


class TokenRefresh(Resource):
    """
    Refreshes access tokens with valid refresh tokens
    """

    @classmethod
    @jwt_refresh_token_required
    def post(cls):
        current_user = get_jwt_identity()
        new_token = create_access_token(current_user._id, fresh=False)
        return {"access_token": new_token}


# For logging out we can use `get_raw_jwt` and use the blacklisting functionality
