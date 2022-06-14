from project import app
from flask import render_template, request, url_for, redirect, Blueprint
from project.persistence.users_dao import get_user_by_passoword


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        print('login POST....')
        email = request.form['email']
        password = request.form['password']
        user = get_user_by_passoword(email, password)
        print("user:",user)
        if user:
            return redirect(url_for('products'))
        else:
            error = "User not found"
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    return 'Logout'