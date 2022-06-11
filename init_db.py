import sqlite3

connection = sqlite3.connect('database.db')

# USERS
with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO Users (fullname, email, birthdate, country, city, address) VALUES (?, ?, ?, ?, ?, ?)",
            ('John doe', 'jd@mia.com','2001-01-01','Spain','Madrid','B Street 1')
            )

cur.execute("INSERT INTO Users (fullname, email, birthdate, country, city, address) VALUES (?, ?, ?, ?, ?, ?)",
            ('Ann Smith', 'as@mia.com', '2010-07-02','England','London','C Street 1')
            )

# PRODUCTS
cur.execute("INSERT INTO Products (name , description , cost, is_active) VALUES (?, ?, ?, ?)",
            ('Product1', 'Description1',50,True)
            )

cur.execute("INSERT INTO Products (name , description , cost, is_active) VALUES (?, ?, ?, ?)",
            ('Product2', 'Description2', 20,True)
            )


connection.commit()
connection.close()