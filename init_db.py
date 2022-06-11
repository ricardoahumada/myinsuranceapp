import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO Users (fullname, email) VALUES (?, ?)",
            ('John doe', 'jd@mia.com')
            )

cur.execute("INSERT INTO Users (fullname, email) VALUES (?, ?)",
            ('Ann Smith', 'as@mia.com')
            )

connection.commit()
connection.close()