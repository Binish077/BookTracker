import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Cinder', 'Content for the first book')
            )

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Scarlet', 'Content for the second book')
            )

connection.commit()
connection.close()