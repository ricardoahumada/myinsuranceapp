import email
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
    conn = get_db_connection()
    users = conn.execute('SELECT * FROM users').fetchall()
    conn.close()
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

        if not fullname:
            flash('Fullname is required!')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO users (fullname, email, birthdate, country, city, address) VALUES (?, ?, ?, ?, ? , ?  )',
                         (fullname, email, birthdate, country, city, address))
            conn.commit()
            conn.close()
            return redirect(url_for('indexuser'))

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

        if not fullname:
            flash('Full name is required!')
        else:
            conn = get_db_connection()
            conn.execute('UPDATE users SET fullname = ?, email = ?, birthdate=?, country=?, city=?, address=? '
                         ' WHERE id = ?',
                         (fullname, email, birthdate, country, city, address, id))
            conn.commit()
            conn.close()
            return redirect(url_for('indexuser'))

    return render_template('user/edit.html', user=user)

@app.route('/users/<int:id>/delete', methods=('POST',))
def deleteuser(id):
    user = get_user(id)
    conn = get_db_connection()
    conn.execute('DELETE FROM users WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    flash('"{}" was successfully deleted!'.format(user['fullname']))
    return redirect(url_for('indexuser'))



""" Routes/Controllers PRODUCTS """
@app.route('/products/')
def products():
    conn = get_db_connection()
    products = conn.execute('SELECT * FROM products').fetchall()
    conn.close()
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
    

        if not name:
            flash('name is required!')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO products (name, description, cost, is_active) VALUES (?, ?, ?, ?)',
                         (name, description, cost, is_active))
            conn.commit()
            conn.close()
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
       
        if not name:
            flash('Full name is required!')
        else:
            conn = get_db_connection()
            conn.execute('UPDATE products SET name = ?, description = ?, cost=?, is_active=?' 
                         ' WHERE id = ?',
                         (name, description, cost, is_active, id))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('product/editproduct.html', product=product)

@app.route('/products/<int:id>/delete', methods=('POST',))
def deleteproduct(id):
    product = get_product(id)
    conn = get_db_connection()
    conn.execute('DELETE FROM products WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    flash('"{}" was successfully deleted!'.format(product['name']))
    return redirect(url_for('index'))