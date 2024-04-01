import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

# adding some default values
cur.execute("INSERT INTO books (title, thoughts) VALUES (?, ?)",
            ('Cinder', 'Best sci-fi book ever!!')
            )

cur.execute("INSERT INTO books (title, thoughts) VALUES (?, ?)",
            ('Atomic Habits', 'Useful and easy to follow')
            )

connection.commit()
connection.close()