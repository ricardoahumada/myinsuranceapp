# -*- coding: utf-8 -*-
__version__ = '0.1'

from project import app
from flask import jsonify
from project.persistence.users_dao import *

@app.route('/api/v1/users/', methods=['GET'])
def api_users():
    users = get_users()
    return jsonify(users)
