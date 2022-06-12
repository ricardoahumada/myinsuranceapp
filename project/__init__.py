# -*- coding: utf-8 -*-
__version__ = '0.1'

from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension

""" App """
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'
app.debug = True
toolbar = DebugToolbarExtension(app)

from project.persistence import *
from project.controllers import *
