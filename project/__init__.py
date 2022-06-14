# -*- coding: utf-8 -*-
__version__ = '0.1'

from flask import Flask
from flask_jwt_extended import JWTManager
from flask_debugtoolbar import DebugToolbarExtension


""" App """
app = Flask(__name__)
app.debug = False
app.config['SECRET_KEY'] = 'super-secret'
toolbar = DebugToolbarExtension(app)

jwt = JWTManager(app)


from project.controllers.web import *
from project.jwt import *
from project.controllers.api import *
