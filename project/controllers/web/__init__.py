# -*- coding: utf-8 -*-
__version__ = '0.1'
from project import app
from flask import render_template, request, url_for, flash, redirect
import os
import glob
from flask import Flask, render_template, redirect, url_for, request

from project.persistence.users_dao import get_user_by_passoword

__all__ = [os.path.basename(
    f)[:-3] for f in glob.glob(os.path.dirname(__file__) + "/*.py")]

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        email = request.form['email']
        password= request.form['password']
        user=get_user_by_passoword(email,password)
        print(user)
        if user:
            return redirect(url_for('users'))
        else:
            error="Not found"
    return render_template('login.html', error=error)

