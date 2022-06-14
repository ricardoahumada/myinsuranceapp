# -*- coding: utf-8 -*-
__version__ = '0.1'
from project import app
import os
import glob
from flask import render_template


__all__ = [os.path.basename(
    f)[:-3] for f in glob.glob(os.path.dirname(__file__) + "/*.py")]


@app.route('/')
def index():
    return render_template('index.html')