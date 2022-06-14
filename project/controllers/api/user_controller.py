# -*- coding: utf-8 -*-
__version__ = '0.1'

from project import app
from flask import jsonify, request
from project.persistence.users_dao import *
from flask_jwt_extended import jwt_required, get_jwt_identity


@app.route('/api/v1/users/', methods=['GET'])
# @jwt_required()
def api_get_users():
    # print(get_jwt_identity)
    users = get_users()
    return jsonify(users)

@app.route('/api/v1/users/<id>', methods=['GET'])
# @jwt_required()
def api_get_user(id):
    # print(get_jwt_identity)
    user = get_user(id)
    return jsonify(user)

@app.route('/api/v1/users/<id>', methods=['DELETE'])
# @jwt_required()
def api_delete_user(id):
    # print(get_jwt_identity)
    delete_user(id)
    return jsonify({'ok': True})

@app.route('/api/v1/users/', methods=['POST'])
def api_post_users():
    # print(get_jwt_identity)
    user = request.json
    print(user)
    create_user(user.fullname, user.email, user.birthdate, user.country, user.city, user.address, user.password)
    return jsonify({'ok': True})
