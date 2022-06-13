# -*- coding: utf-8 -*-
__version__ = '0.1'

from project import app
from flask import render_template, request, url_for, flash, redirect
import os
import glob
__all__ = [os.path.basename(
    f)[:-3] for f in glob.glob(os.path.dirname(__file__) + "/*.py")]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')
