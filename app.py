import email
import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort

""" DAO """
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_user(user_id):
    conn = get_db_connection()
    user = conn.execute('SELECT * FROM users WHERE id = ?',
                        (user_id,)).fetchone()
    conn.close()
    if user is None:
        abort(404)
    return user

""" App """
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'
app.debug = True


""" Routes/Controllers """
@app.route('/')
def index():
    conn = get_db_connection()
    users = conn.execute('SELECT * FROM users').fetchall()
    conn.close()
    return render_template('index.html', users=users)

@app.route('/<int:user_id>')
def user(user_id):
    theuser = get_user(user_id)
    return render_template('user.html', user=theuser)

@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        fullname = request.form['fullname']
        email = request.form['email']

        if not fullname:
            flash('Fullname is required!')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO users (fullname, email) VALUES (?, ?)',
                         (fullname, email))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('create.html', user=user)

@app.route('/<int:id>/edit', methods=('GET', 'POST'))
def edit(id):
    user = get_user(id)

    if request.method == 'POST':
        fullname = request.form['fullname']
        email = request.form['email']

        if not fullname:
            flash('Full name is required!')
        else:
            conn = get_db_connection()
            conn.execute('UPDATE users SET fullname = ?, email = ?'
                         ' WHERE id = ?',
                         (fullname, email, id))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('edit.html', user=user)

@app.route('/<int:id>/delete', methods=('POST',))
def delete(id):
    user = get_user(id)
    conn = get_db_connection()
    conn.execute('DELETE FROM users WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    flash('"{}" was successfully deleted!'.format(user['fullname']))
    return redirect(url_for('index'))