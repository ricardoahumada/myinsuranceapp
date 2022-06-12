import sqlite3

connection = sqlite3.connect('database.db')

# USERS
with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO Users (fullname, email, birthdate, country, city, address, password) VALUES (?, ?, ?, ?, ?, ?, ?)",
            ('John doe', 'jd@mia.com','2001-01-01','Spain','Madrid','B Street 1','password2')
            )

cur.execute("INSERT INTO Users (fullname, email, birthdate, country, city, address, password) VALUES (?, ?, ?, ?, ?, ?, ?)",
            ('Ann Smith', 'as@mia.com', '2010-07-02','England','London','C Street 1','password2')
            )

# PRODUCTS
cur.execute("INSERT INTO Products (name , description , cost, is_active, user) VALUES (?, ?, ?, ?, ?)",
            ('Product1', 'Description1',50,True,2000)
            )

cur.execute("INSERT INTO Products (name , description , cost, is_active, user) VALUES (?, ?, ?, ?, ?)",
            ('Product2', 'Description2', 20,True,130)
            )


connection.commit()
connection.close()