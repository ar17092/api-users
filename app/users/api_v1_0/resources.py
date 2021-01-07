from flask import request, Blueprint, jsonify
from flask_restful import Api, Resource
import json

from .schemas import UserSchema
from ..models import User
from app.common.error_handling import ObjectNotFound

users_bp = Blueprint('users_bp', __name__)
user_schema = UserSchema()

api = Api(users_bp)

class UserListResource(Resource):
    def get(self):
        users = User.get_all()
        result = user_schema.dump(users, many=True)
        return result

    def post(self):
        data = request.get_json()
        print("============================================================>",data)
        user_dict = user_schema.load(data)
        user = User(name=user_dict['name'],
                    email=user_dict['email'],
                    password=user_dict['password'])
        user.save()

        resp = user_schema.dump(user)
        return resp, 201

class UserResource(Resource):
    def get(self, email):
        user = User.get_by_email(email=email)
        if user is None:
            return jsonify({"Error":"No existe el usuario"})
        resp = user_schema.dump(user)
        return resp

api.add_resource(UserListResource,'/RestServer_Java-PeopleData/resources/datos/findAll', endpoint='user_list_source')

api.add_resource(UserResource, '/RestServer_Java-PeopleData/resources/datos/<string:email>', endpoint='user_resource')
