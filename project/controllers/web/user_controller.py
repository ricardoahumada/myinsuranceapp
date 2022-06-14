# -*- coding: utf-8 -*-
__version__ = '0.1'

from project import app
from flask import render_template, request, url_for, flash, redirect
from project.persistence.users_dao import *


@app.route('/users/')
def users():
    users = get_users()
    return render_template('user/users.html', users=users)

@app.route('/users/<int:user_id>')
def user(user_id):
    theuser = get_user(user_id)
    return render_template('user/user.html', user=theuser)

@app.route('/users/create', methods=('GET', 'POST'))
def createuser():
    if request.method == 'POST':
        app.logger.info(request.form)
        fullname = request.form['fullname']
        email = request.form['email']
        birthdate= request.form['birthdate']
        country= request.form['country']
        city= request.form['city']
        address= request.form['address']
        password= request.form['password']

        if not fullname:
            flash('Fullname is required!')
        else:
            create_user(fullname, email, birthdate, country, city, address,password)
            return redirect(url_for('users'))

    return render_template('user/create.html', user=user)

@app.route('/users/<int:id>/edit', methods=('GET', 'POST'))
def edituser(id):
    user = get_user(id)

    if request.method == 'POST':
        fullname = request.form['fullname']
        email = request.form['email']
        birthdate= request.form['birthdate']
        country= request.form['country']
        city= request.form['city']
        address= request.form['address']
        password= request.form['password']

        if not fullname:
            flash('Full name is required!')
        else:
            edit_user(fullname, email, birthdate, country, city, address, password, id)
            return redirect(url_for('users'))

    return render_template('user/edit.html', user=user)

@app.route('/users/<int:id>/delete', methods=('POST',))
def deleteuser(id):
    user = get_user(id)
    delete_user(id)
    flash('"{}" was successfully deleted!'.format(user['fullname']))
    return redirect(url_for('users'))
