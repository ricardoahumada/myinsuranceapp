import email
from pickle import TRUE
import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort

""" DAO """
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_product(product_id):
    conn = get_db_connection()
    product = conn.execute('SELECT * FROM products WHERE id = ?',
                        (product_id,)).fetchone()
    conn.close()
    if product is None:
        abort(404)
    return product

def get_user(user_id):
    conn = get_db_connection()
    user = conn.execute('SELECT * FROM users WHERE id = ?',
                        (user_id,)).fetchone()
    conn.close()
    if user is None:
        abort(404)
    return user

def get_users():
    conn = get_db_connection()
    users = conn.execute('SELECT * FROM users').fetchall()
    conn.close()
    return users
def get_products():
    conn = get_db_connection()
    products = conn.execute('SELECT * FROM products').fetchall()
    conn.close()
    return products

def create_user(fullname, email, birthdate, country, city, address,password):
    conn = get_db_connection()
    conn.execute('INSERT INTO users (fullname, email, birthdate, country, city, address,password) VALUES (?, ?, ?, ?, ? , ?,?  )',
                         (fullname, email, birthdate, country, city, address,password))
    conn.commit()
    conn.close()
    return True
def edit_user(fullname, email, birthdate, country, city, address, password, id):
    conn = get_db_connection()
    conn.execute('UPDATE users SET fullname = ?, email = ?, birthdate=?, country=?, city=?, address=?,password=? '
                         ' WHERE id = ?',
                         (fullname, email, birthdate, country, city, address, password, id))
    conn.commit()
    conn.close()
    return True
def delete_user(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM users WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return True

def create_product(name, description, cost, is_active, user):
    conn = get_db_connection()
    conn.execute('INSERT INTO products (name, description, cost, is_active,user) VALUES (?, ?, ?, ?, ?)',
                         (name, description, cost, is_active, user))
    conn.commit()
    conn.close()
    return True
def edit_product(name, description, cost, is_active,user, id):
    conn = get_db_connection()
    conn.execute('UPDATE products SET name = ?, description = ?, cost=?, is_active=?,user= ?'
                         ' WHERE id = ?',
                         (name, description, cost, is_active,user, id))
    conn.commit()
    conn.close()
    return True
def delete_product(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM products WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return True
""" App """
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'
app.debug = True


""" Routes/Controllers ROOT """
@app.route('/')
def index():
    return render_template('index.html')

""" Routes/Controllers USER """
@app.route('/users/')
def users():
    users = get_users()
    return render_template('user/index.html', users=users)

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



""" Routes/Controllers PRODUCTS """
@app.route('/products/')
def products():
    products = get_products()
    return render_template('product/indexproduct.html', products=products)

@app.route('/products/<int:product_id>')
def product(product_id):
    theproduct = get_product(product_id)
    return render_template('product/product.html', product=theproduct)

@app.route('/products/create', methods=('GET', 'POST'))
def createproduct():
    if request.method == 'POST':
        app.logger.info(request.form)
        name = request.form['name']
        description = request.form['description']
        cost= request.form['cost']
        is_active= request.form['is_active']
        user= request.form['user']


        if not name:
            flash('name is required!')
        else:
            create_product(name, description, cost, is_active, user)
            return redirect(url_for('index'))

    return render_template('product/createproduct.html', product=product)

@app.route('/products/<int:id>/edit', methods=('GET', 'POST'))
def editproduct(id):
    product = get_product(id)

    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        cost= request.form['cost']
        is_active= request.form['is_active']
        user= request.form['user']
       
        if not name:
            flash('Full name is required!')
        else:
            edit_product(name, description, cost, is_active,user, id)
            return redirect(url_for('index'))

    return render_template('product/editproduct.html', product=product)

@app.route('/products/<int:id>/delete', methods=('POST',))
def deleteproduct(id):
    product = get_product(id)
    delete_product(id)
    flash('"{}" was successfully deleted!'.format(product['name']))
    return redirect(url_for('index'))